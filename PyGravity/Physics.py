from decimal import *
from Particle import Particle
from Vector import Vector

##
#@file ./PyGravity/Physics.py
#@author Russell Loewe russloewe@gmail.com
#@date 6-29-2015
#
#@brief Main Physics engine for calculating forces
#todo remove Physics.objects to seperate class
#
#The Physics class contains methods for finding the force of 
#gravity between two objects, or between an array of objects. 
#For finding acceleration due to gravity between two objects, 
#or between an array of objects.
#For calculating the escape velocity between two objects or 
#an array of objects.
#And for applying and stepping all particles in the objects list
#@todo Remove need to creat class instance. move and object list to 
#

class Physics(object):
		##
		#@brief Physics Class.
		#This class defines the Physics object.
		#Creating a physics object to hold physics attributes and object list

		#seperate object.
		#
 
	def __init__(self):
		self.objects = []
		self.timestep = 1
		self.total_steps = 0
		self.dimension = 3
		self.set_prec(100)
		self.fast = True
		##
		#@brief inits with default values and empty lists

	def set_prec(self, a):
		getcontext().prec = a
		##
		#@brief change default precision for Vector
		#


	def Fg(self, A, B):
		G = Decimal('6.67384e-11')
		r =  A.P - B.P   #vector between two particles
		r_squared = r.magnitude() ** 2  # dist between A, B squared
		f_mag = (G*A.m.magnitude()*B.m.magnitude())*(r_squared**(-1))
		f_vec = r.unit() * f_mag
		return f_vec
		##
		#@brief calculate force of gravity between two particles
		#@param A first PyGravity.Particle.Particle object
		#@param B second PyGravity.Particle.Particle object
		#@see PyGravity.Particle.Particle
		#@returns Force of gravity as a vector
		#@see PyGravity.Vector.Vector
		#
		#This method takes two Particle Objects and calculates the 
		#force of gravity between the two of them using Newtons 
		#classical law of gravity.
		#@see PyGravity.Vector.Vector.__sub__() , 
		#PyGravity.Vector.Vector.magnitude()
		#

	def sum_Fg_one_particle(self, A):
		force_list = []
		for particle in self.objects:
			if particle != A:
				force_list.append(self.Fg(particle, A))
		f = lambda a,b: a+b
		total_force = reduce(f, force_list)
		return total_force
		##
		#@brief Calculates the total force of gravity in the entire
		#system acting on one particle.
		#@param A PyGravity.Particle.Particle object
		#@return total_force, as a Vector
		#
		#This function takes a single Particle object and iterates through
		# the whole object list using
		#Physics.Fg() function to find the total force 
		#acting on a single Particle.

	#find acceleration from total force, apply using Particle.accelerate()
	def apply_gravitational_acceleration(self, A):
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
		return r * acc
		##
		#@brief Directly find acceleration from gravity between two particles.
		#@param A PyGravity.Vector.Vector object
		#@param B PyGravity.Vector.Vector object
		#@return Acceleration Vector
		#@see PyGravity.Vector.Vector
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

    #find escape velocity between 2 objects
	def escape_v(self, A, B):
		G = Decimal('6.67384e-11')
		r = (A.P-B.P).magnitude() #distance between A and B
		esc = ((G*B.m[0])/r).sqrt()
		return esc

	def total_escape_v(self, A):
		esc_list = []
		for item in self.objects:
			if A != item:
				esc_list.append(self.escape_v(A, item))
		return reduce(lambda a,b: a+b, esc_list)

	def escaping(self):
		escaping = []
		for item in self.objects:
			total_esc = self.total_escape_v(item)
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




