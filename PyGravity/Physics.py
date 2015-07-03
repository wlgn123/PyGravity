from decimal import *
from Particle import Particle
from Vector import Vector
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
		'''
		inits with default values and empty lists
		'''
		self.objects = []
		self.timestep = 1
		self.total_steps = 0
		self.dimension = 3
		self.set_prec(100)
		self.fast = True


	def set_prec(self, a):
		'''
		:param: (int) precision value for vectors
			set precision for vectors
		
		.. todo:: move to outside container
		
		'''
		getcontext().prec = a



	def Fg(self, A, B):
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


	def sum_Fg_one_particle(self, A):
		'''
		Finds the the total force of gravity acting on one particle. 
		The force of gravity acting on the supplied particle is claculated 
		for every particle in the global particle list. The result is then 
		summed and returned.
		
		:param: A(Particle): Particle for which the force of gravity is 
			being calculated.
		
		:returns: Force of gravity as a Vector Object.
		
		.. todo:: fix stupid method name
		'''
		force_list = []
		for particle in self.objects:
			if particle != A:
				force_list.append(self.Fg(particle, A))
		f = lambda a,b: a+b
		total_force = reduce(f, force_list)
		return total_force

	#find acceleration from total force, apply using Particle.accelerate()
	def apply_gravitational_acceleration(self, A):
		'''
		Calculates the acceleration action on a particle using the 
		sum_fg_one_particle() method and f=ma then applies the acceleration 
		to the particle using the Particle.accelerate() method
		
		:param: A(Particle): Particle to apply acceleration to
		
		'''
		total_Fg_A = self.sum_Fg_one_particle(A)
		acceleration = total_Fg_A * (1/A.m.magnitude())
		A.accelerate(acceleration,self.timestep)
		##
		#@brief Accelerate a Particle .
		#@param A PyGravity.Particle.Particle
		#@return null
		#
		#Takes a Particle object and uses Physics.sum_Fg_one_particle()
		#to find the force on the particle. Then uses's Netown's 
		#F=ma to find the acceleration acting on the particle. Then 
		#calls the Particle.accelerate() method to apply the acceleration 
		#to the particle
		#

    # more direct way to find acceleration, skipping some steps
	def calculate_acc(self,A, B):
		G = Decimal('6.67384e-11')
		r =  A.P - B.P   #vector between two particles
		r_cube = r.magnitude() ** 3  # dist between A, B cubed
		acc = G * B.m[0] / r_cube
		return r * acc #r.unit()?
		##
		#@brief Directly find acceleration from gravity between two particles.
		#@param A PyGravity.Vector.Vector object
		#@param B PyGravity.Vector.Vector object
		#@return Acceleration Vector
		#@see PyGravity.Vector.Vector
		#@todo displacement vector times accelerating magnitude needs to
		#be the unit displacment vector time acceleration magnitued 
		#r -> r.unit()
		#
		#This function calculates the force of gravity between two particles
		#directly, skipping the uneeded math steps such as needing to 
		#find the force of gravity.

    #adding all acceleration vectors and using Particle.accelerate()
	def fast_accelerate(self, A):
		acc_list = []
		for particle in self.objects:
			if particle != A:
				acc_list.append(self.calculate_acc(particle, A))
		total_acc = reduce(lambda a,b:a+b, acc_list)
		A.accelerate(total_acc, self.timestep)
		##
		#@brief Takes a particle and calculates the net acceleration
		#@param A PyGravity.Particle.Particle
		#@return Acceleration Vector
		#@see PyGravity.Vector.Vector
		# Uses Physics.calculate_acc() and sums over all objects in 
		#the object list to produce the net accleration on Particle A
		#

    #find escape velocity between 2 objects
	def escape_v(self, A, B):
		G = Decimal('6.67384e-11')
		r = (A.P-B.P).magnitude() #distance between A and B
		esc = ((G*B.m[0])/r).sqrt() # formula for escape velocity
		return esc
		##
		#@brief Find the Gravitational Escape Velocity
		#@param A PyGravity.Particle.Particle 
		#@param B PyGravity.Particle.Particle
		#@return escape velocity for particle A to escape from Particle B
		#
		#Calculates the escape velocity required for object A to escape 
		#from object B

	def total_escape_v(self, A):
		esc_list = []
		for item in self.objects:
			if A != item:
				esc_list.append(self.escape_v(A, item))
		return reduce(lambda a,b: a+b, esc_list)
		##
		#@brief Find escape velocity for particle A
		#@param A PyGravity.Particle.Particle
		#@return escape velocity as vector object
		#
		#Takes a particle and claculates the escape velocity required to 
		#escape all object in the object list.
		#@see Physics.escape_v()

	def escaping(self):
		escaping = []
		for item in self.objects:
			total_esc = self.total_escape_v(item)
			if total_esc <= item.V.magnitude():
				escaping.append(item.name)
		return escaping
		##
		#@brief Find all objects going fast enough to escape the system
		#@return list of all objects escaping the system
		#
		#This function when invoked will iterate through all Particle
		#objects in the objects list, calculate the escape velocity 
		#required for that particle to escape the system, then adds 
		#that particle to a list if it is going faster than the escape
		#veloctity. After iterating through all objects, a list is 
		#returned wich lists all objects that are escaping from the 
		#system of particles
		#


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




