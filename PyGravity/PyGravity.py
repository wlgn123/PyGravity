import Physics
import Data_IO
import sys

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
		 
		:param: file_name(string) Name of dat
		
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
		
		.. todo:: fix this function. it is completly fucked.
		'''
		self.writer.objects = self.particle_list
		self.writer.write_file(file_name)

	def step_all_verlet(self):
		'''
		Using the Verlet veoloicy method for updating the particles 
		position. This method also uses the Proto_Accel and half_list 
		method to reduce calculations by half. This method runs about 
		twice as fast as the multi-core step_all method for set of 40 
		points.
		
		'''
		
		
		p_len = len(self.particle_list) 
		half_list= []
		for I in range(p_len):
			for i in range(I+1, p_len):
				half_list.append((self.particle_list[I],self.particle_list[i]))
		
		for pair in half_list:
			try:
				Physics._step_verlet_one(pair, self.time_interval)
				Physics._step_verlet_two(pair, self.time_interval)
			except RuntimeWarning as e:
				print e
				sys.exit(1)
				

		

			
	def step_all(self):
		'''
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
		for item in self.particle_list:
			try:
				Physics._step_euler(self.particle_list, self.fast,self.time_interval, item)
			except RuntimeWarning as e:
				print e 
				
		
		


