'''
.. module:: Global_Container
   :platform: Unix
   :synopsis: Global.

.. moduleauthor:: Russell Loewe <russloewe@gmail.com>

'''
class Global_Container(object):
	'''
	Class to create Global container of values. Here the PyGravity 
	module will store the list of active Particles in the system,
	as well as the time increment, the total time elapsed, the 
	spatial demisnion for the simulation, and the precision for the 
	vectors. 
	'''
	
	def __init__(self):
		'''
		Intits the values. Defaults dimension to 3, timestep to 1,
		time elapsed to 0, particle list to an empty list and precision 
		to 200.
		'''
		self.particle_list = []
		self.dimension = 3
		self.time_inc = 1
		self.total_time = 0
		self.precision = 200

	def step_time(self):
		'''
		increases the currant time by the time_inc
		'''
		self.total_time = self.total_time + self.time_inc
		
	def add_particle(self, particle):
		'''
		adds particle to list of current particles
		
		:param: particle(Particle): Particle to add
		'''
		self.particle_list.append(particle)
		
	def remove_particle(self, particle):
		'''
		Remove particle from current list
		
		:param: particle(particle): Particle to be deleted.
		'''
		new_list = []
		for item in self.particle_list:
			if item != particle:
				new_list.append(item)
		self.particle_list = new_list
		
	def set_time_interval(self, interval):
		'''
		Change the time interval for the simulator
		
		:param: interval(int): New interval value.
		'''
		self.time_inc = interval
		
	def set_prec(self, precision):
		'''
		Change global precision for vectors.
		
		:param: precision(int): New precision.
		
		'''
		self.precision = precision
		
	def set_dimension(self, dim):
		'''
		Change the default precision.
		
		:param: dim(int): New Dimension.
		'''
		self.dimension = dim
