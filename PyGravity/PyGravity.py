import Physics
import Data_IO

'''
.. module:: PyGravity
   :platform: Unix
   :synopsis: Main PyGravity mod.

.. moduleauthor:: Russell Loewe <russloewe@gmail.com>

'''
class PyGravity():
	'''Main class for  combining submodules
	'''
	def __init__(self):
		'''initialize data reader and writer
		Also set global diminsion
		''' 
		self.reader = Data_IO.Reader()
		self.writer = Data_IO.Writer()
		#particels in active simulation
		self.particle_list = []
		#time stuff
		self.time_interval = 1.0
		self.initial_time = 0
		self.currant_time = 0
		#vector dimensions
		self.dimension = 3
		#use faster extension,
		self.fast =  False
		
	def set_fast(self, booln):
		'''
		Sets falg so the faster grav_accel function is used.
		Just a stand in until new extension is complete and tested.
		'''
		if booln == True:
			self.fast =  True
		elif booln == False:
			self.fast = False
		else:
			raise TypeError("Only True or False boolean accepted")
		


	def set_dimension(self, dim):
		'''Set global dimension
		
		Dimension is defaulted to 3, but can be overriden here
		
		.. code-block:: python
		
			PyGravity.set_dimension(4)
		
		:param: (int) The diminsion of the vectors

		'''
		self.dimension = dim

	def set_time_interval(self, interval):
		'''
		Adjust the time step of the currant simulation. 
		
		:param: interval(int): Interval to use
		
		'''
		self.time_interval = float(interval)


	def add_particle(self, particle):
		'''
		add a particle to the list of active particles. The particles
		is compared to existing particles. If a particle name is already 
		used the addition will be deined. 
		
		:param: particle(Particle Object): particle to add.
		
		:returns: none
		
		:raises: ValueError if particle name already exists in 
			particle_list.
		'''
		if len(self.particle_list) == 0:
			self.particle_list.append(particle)
		else:
			for item in self.particle_list:
				if item.name == particle.name:
					raise ValueError('particle name already present')
				self.particle_list.append(particle)
				break



	def read_file(self, file_name):
		''' 
		Use to load a set of particles from a CSV data file, 
		The particles are then loaded into the objects list
		under Physics.objects.
		 
		:param: file_name(string) Name of dat		.. todo:: iterate through once, update position, iterate a second
			time to do the velocitya file to be read.
		
		
		:py:func:'PyGravity.set_dimension'
		
		.. note::
			the dimension of the PyGravity.dimension must match the 
			the dimension of the particles in the CSV file.
		
		.. todo:: figure out sphinx references
		
		'''
		self.reader.read_file(file_name)
		for item in self.reader.objects:
			self.add_particle(item)


	def write_file(self, file_name):
		'''
		Write current particle set to output file
		
		:param: (string)file_name File name and path to write current
			dataset
		
		'''
		self.writer.objects = self.particle_list
		self.writer.write_file(file_name)

	def step_all_verlet(self):
		'''
		Using the Verlet veoloicy method for updating the particles 
		position
		
		
		.. todo:: new particle method that does not use the time_interval. 
			it is just uneeded computation when using verlet or rk4 methods.
			
		'''
		
		for item in self.particle_list:
			acceleration  = Physics.Sum_Grav_Accel(self.particle_list, item, self.fast)
			#print 'Acc: ', acceleration.round(2)
			new_p = item.P + item.V*self.time_interval + acceleration*(1.0/2.0)*self.time_interval**2
			item.P = new_p
			#print 'Pos: ',new_p.round(2)
			item.store_acc(acceleration)
		for item in self.particle_list:
			new_acceleration = Physics.Sum_Grav_Accel(self.particle_list, item, self.fast)
			#print 'new acc',new_acceleration.round(2)
			item.accelerate((item.A + new_acceleration)*(self.time_interval/2.0), 1.0)
			#item.V = new_v

	def step_all_verlet_multi(self):
		'''
		Multicore Verlet method, assumes time_interval of 1
		'''
		p_len = len(self.particle_list)
		half_list = []
		for I in range(p_len):
			for i in range(I+1, p_len):
				half_list.append((self.particle_list[I],self.particle_list[i]))
		print half_list
			
		from multiprocessing import Pool
		pool = Pool()
		pool.map(step_verlet_one, half_list)
		pool.join()
		pool.map(step_verlet_two, half_list)
		pool.join()
		pool.close()
		

			
	def step_all(self):
		'''		.. todo:: iterate through once, update position, iterate a second
			time to do the velocity
		Iterates through all the particles in self.particle_list and
		runs the Physics.Sum_Grav_Accel() function, and applies the 
		acceleration to update each particle's velocity vector, then 
		finally iterates through each particle and moves that particle
		moving the new velocity.
		
		.. note:: The acceleration is applied to the velocity using the
			time interval. Thus the new velocity equals the currant
			velocity plus the acceleration times the time_interval. 
			The same procedure produces the new position using the same 
			time_interval.
			
		
		'''
		from multiprocessing import Pool
		from functools import partial
		pool = Pool()
		
		Step = partial(step, self.particle_list, self.fast, self.time_interval)
		
		pool.map(Step, self.particle_list)
		
		pool.close()
		pool.join()
		
		self.currant_time += self.time_interval
		
def step(part_list, flag, time_interval, i):
	acc = Physics.Sum_Grav_Accel(part_list, i, flag)
	i.accelerate(acc, time_interval)
	i.move(time_interval)

def step_verlet_one(pair):
	A, B = pair
	proto = Physics.Proto_Acc(A, B)
	A_acc = proto * B.m
	B_acc = (-1.0)* proto * A.m
	A.store_acc(A_acc)
	B.store_acc(B.acc)
	A.P = A.P + A.V *time_interval + A_acc*(1.0/2.0)
	B.P = B.P + B.V *time_interval + B_acc*(1.0/2.0)
	
def step_verlat_two(pair):
	A, B = pair
	proto = Physics.Proto_Acc(A, B)
	A_acc = proto * B.m
	B_acc = proto* (-1.0) * A.m
	A.V = (A.store + A_acc)/(2.0) 
	B.V = (B.store + A_acc)/2.0
