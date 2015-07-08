from decimal import *
import Particle
import Global_Container
import Vector
'''
.. module:: Physics
   :platform: Unix
   :synopsis: Main Physics Function Bundle.

.. moduleauthor:: Russell Loewe <russloewe@gmail.com>
.. todo:: 
	Create a seperate object to hold particle list, vector deminsion
	and time step and time counter
'''
class Physics(object):
	"""Physics class
	This class holds the particle object and varies atributes for the 
	system
	
	.. todo:: make static module, out attributes and paticle list into 
		seperate container
	
	"""

	def __init__(self):
		pass


	@staticmethod
	def Grav_Force(A, B):
		'''
		Calculates the force of gravity between two particles. Uses Newton's 
		Law of Gravity. Gravitational constant is in standtard metric units.
		
		:param: A(Particle): First particle
		
		:param: B(Particle): Second Particle
		
		:returns: Force(Vector): Force acting on particle A as a Vector.
		
		.. todo:: abstract gravitational constant to Global Cantainer, 
			add parser to PyGravity to smartly determin working units.
		
		'''
		G = Decimal('6.67384e-11')
		r =  A.P - B.P   #vector between two particles
		r_squared = r.magnitude() ** 2  # dist between A, B squared
		f_mag = (G*A.m.magnitude()*B.m.magnitude())*(r_squared**(-1))
		f_vec = r.unit() * f_mag
		return f_vec

	@staticmethod
	def Total_Grav_Force(global_container, particle):
		'''
		Finds the the total force of gravity acting on one particle. 
		The force of gravity acting on the supplied particle is claculated 
		for every particle in the global particle list. The result is then 
		summed and returned.
		
		:para: particle_list(list): List of particle objects
		
		:param: parrticle(Particle): Particle for which the force of gravity is 
			being calculated.
		
		:returns: Force of gravity as a Vector Object.
		
		'''
		force_list = []
		for _particle in global_container.particle_list:
			if _particle != particle:
				force_list.append(self.Grav_Force(_particle, particle))
		f = lambda a,b: a+b
		total_force = reduce(f, force_list)
		return total_force

	#find acceleration from total force, apply using Particle.accelerate()


    # more direct way to find acceleration, skipping some steps
	@staticmethod
	def Grav_Accel(A, B):
		'''
		Calculate the acceleration between particle A and B due to 
		gravity. Uses math shortcuts to reduce total number of calculations
		as apposed to using Grav_Force / mass to find acceleration.
		
		:param: A(Vector): The first vector.
		:param: B(Vector): The second vector.
		
		:returns: The acceleration as a Vector Object.
		
		.. todo:: Add formated math example
		
		.. todo:: double check math on the return vector, see comment.
		'''
		G = Decimal('6.67384e-11')
		r =  A.P - B.P   #vector between two particles
		r_cube = r.magnitude() ** 3  # dist between A, B cubed
		acc = G * B.m[0] / r_cube
		return r * acc #r.unit()?

	@staticmethod
	def Sum_Grav_Accel(global_container, A):
		'''
		Sum the total acceleration acting on a particle by using the 
		Grav_Accel function and iterating through the particle list
		
		:param: global_container(Global_Container): List of particles 
			to iteratethrough.
		
		:param: A(Vector): Vector to calculate acceleration for.
		
		:returns: Acceleraton as a Vector Object
		'''
		acc_list = []
		for particle in global_container.particle_list:
			if particle != A:
				acc_list.append(Grav_Accel(particle, A))
		total_acc = reduce(lambda a,b:a+b, acc_list)
		return total_acc


	@staticmethod
	def Escape_Volecity(A, B):
		'''
		Calculate the escape velocity between two objects. 
		
		:param: A(Particle): First particle.
		
		:param: B(Particle): Second particle.
		
		:returns: Escape velocity as a Vector Object.
		'''
		G = Decimal('6.67384e-11')
		r = (A.P-B.P).magnitude() #distance between A and B
		esc = ((G*B.m[0])/r).sqrt() # formula for escape velocity
		return esc

	@staticmethod
	def Total_Escape_Velocity(global_container, A):
		'''
		Find the total escape velocity acting on a particle with repect 
		to the rest of the active particles in the simulation.
		
		:param: global_containter(Global_Container): Attribute container.
		
		:param: A(Vector): Particle to find escape velocity for.
		
		'''
		esc_list = []
		for item in global_container.particle_list:
			if A != item:
				esc_list.append(self.escape_v(A, item))
		return reduce(lambda a,b: a+b, esc_list)
		
	@staticmethod
	def escaping(global_container):
		'''
		Find all the particles in the currant system that are exceeding 
		the escape velocity for said system of particles
		
		:param: global_container(Global_Container): Container object for 
			particles.
		
		:returns: List of particles exceeding escape velocity.
		'''
		escaping = []
		for item in global_container.perticle_list:
			total_esc = self.Total_Escape_Velocity(item)
			if total_esc <= item.V.magnitude():
				escaping.append(item.name)
		return escaping


	def step_all(self):
		for item in self.objects:
			if self.fast == True:
				self.fast_accelerate(item)
			else:
				self.apply_gravitational_acceleration(item)
		for item in self.objects:
			item.move(self.timestep)
		self.total_steps += 1
		##
		#@brief apply the force of gravity to all objects in the system




