import Particle
import Global_Container
from math import sqrt
import numpy as np
from pygravity_grav_accel import grav_accel
'''
.. module:: Physics
   :platform: Unix
   :synopsis: Main Physics Function Bundle.

.. moduleauthor:: Russell Loewe <russloewe@gmail.com>
.. todo::
	Create a seperate object to hold particle list, vector deminsion
	and time step and time counter
'''


def Grav_Force(A, B):
	'''
	Calculates the force of gravity between two particles. Uses Newton's
	Law of Gravity. Gravitational constant is in standtard metric units.

	:param: A(Particle): First particle

	:param: B(Particle): Second Particle

	:returns: Force(Vector): Force acting on particle A as a Vector.
	'''

	G = -6.67384e-11
	r =  np.subtract(A.P , B.P)   #vector between two particles
	r_norm = np.linalg.norm(r)
	r_squared = r_norm ** 2  # dist between A, B squared
	f_mag = (G*A.m * B.m)*(r_squared**(-1))
	f_vec = r  * (f_mag/r_norm)
	return f_vec

def Total_Grav_Force(particle_list, particle):
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
	for _particle in particle_list:
		if _particle != particle:
			force_list.append(Grav_Force(_particle, particle))
	f = lambda a,b: a+b
	total_force = reduce(f, force_list)
	return total_force

#find acceleration from total force, apply using Particle.accelerate()


# more direct way to find acceleration, skipping some steps

def Grav_Accel(A, B):
	'''
	Calculate the acceleration between particle A and B due to
	gravity. Uses math shortcuts to reduce total number of calculations
	as apposed to using Grav_Force / mass to find acceleration.

	:param: A(Vector): The first vector.
	:param: B(Vector): The second vector.

	:returns: The acceleration as a Vector Object.
	
	.. note:: Force returned is the force acting on B, the second
		argument.
		
		
	.. todo:: Add formated math example, ie learn sphinx embedded math
	
	.. todo:: double check consistancy of (A,B) accross all physics 
		functions
	
	'''
	G = -6.67384e-11
	r =  np.subtract(A.P , B.P)   #vector between two particles
	r_norm = np.linalg.norm(r)
	r_cube = r_norm ** 3  # dist between A, B cubed
	acc = G * B.m / r_cube
	return r * acc # the normilizer, r.unit, is hidden in r_cube

def C_Grav_Accel(A, B):
	'''
	Wrapper for the pygravity_grav_accel extension. Does same thing as 
	the Grav_Accel function but in pre-compiled C.
	
	:param: A(Particle) first particle
	:param: B(Particle) second particle
	:returns: Acceleration as a Vector
	
	.. note:: This wrapps the c extension: pygravity_grav_accel.grav_accel.
	
	The call signature for grav_accel() is as follows:
	
	.. code-block:: python
	
		grav_accel( 
			precision(int),
			mass(string),
			A.x(string),
			A.y(string),
			A.z(string),
			B.x(string),
			B.y(string),
			B.z(string)
			)
	
		
	'''
	acc_string = grav_accel(
							B.m,
							A.P[0],
							A.P[1],
							A.P[2],
							B.P[0],
							B.P[1],
							B.P[2]
							)
	acc = np.array(list(acc_string))
	return acc
	

def Proto_Acc(A,B):
	'''
	Calculate the acceleration between two objects,
	leaving the mass part out. Therefore:
	
	.. code-block:: python
	
		A = Obj1
		B = Obj2
		proto = Proto_Acc(A, B)
		A_Acc = proto * B.mass         #Acceleration on A
		B_Acc = proto * (-1.0)*A.mass   # Acceleration on B
	
	Seperating the calculations into two steps like this will allow 
	for optinmizing acceleration calculations for a large set of 
	objects.
	'''
	G = -6.67384e-11
	r =  A.P - B.P 
	r_mag = np.linalg.norm(r)   # r_mag = ||A-B||
	r_mag_cubed = r_mag * r_mag*r_mag
	
	return r *(G/r_mag_cubed)
	
def Sum_Grav_Accel(particle_list, A, fast_flag = False):
	'''
	Sum the total acceleration acting on a particle by using the
	Grav_Accel function and iterating through the particle list.

	:param: global_container(Global_Container): List of particles
		to iteratethrough.

	:param: A(Vector): Vector to calculate acceleration for.

	:returns: Acceleraton as a Vector Object
	'''
	if(fast_flag):
		acc_list = []
		for particle in particle_list:
			if particle != A:
				acc_list.append(C_Grav_Accel(A, particle))
		total_acc = reduce(lambda a,b:a+b, acc_list)
		return total_acc
	else:
		acc_list = []
		for particle in particle_list:
			if particle != A:
				acc_list.append(Grav_Accel(A,particle))
		total_acc = reduce(lambda a,b:a+b, acc_list)
		return total_acc


def Escape_Velocity(A, B):
	'''
	Calculate the escape velocity between two objects.

	:param: A(Particle): First particle.

	:param: B(Particle): Second particle.

	:returns: Escape velocity as a Vector Object.
	'''
	G = 6.67384e-11
	r = np.linalg.norm(A.P-B.P) #distance between A and B
	esc = sqrt( (G*B.m)/r ) # formula for escape velocity
	return esc


def Total_Escape_Velocity(particle_list, A):
	'''
	Find the total escape velocity acting on a particle with repect
	to the rest of the active particles in the simulation.

	:param: global_containter(Global_Container): Attribute container.

	:param: A(Vector): Particle to find escape velocity for.

	'''
	esc_list = []
	for item in particle_list:
		if A != item:
			esc_list.append(Escape_Velocity(A, item))
	return reduce(lambda a,b: a+b, esc_list)


def escaping(particle_list):
	'''
	Find all the particles in the currant system that are exceeding
	the escape velocity for said system of particles

	:param: global_container(Global_Container): Container object for
		particles.

	:returns: List of particles exceeding escape velocity.
	'''
	escaping = []
	for item in particle_list:
		total_esc = Total_Escape_Velocity(particle_list, item)
		if total_esc < item.V.magnitude():
			escaping.append(item.name)
	return escaping




def step_verlet_one(pair):
	'''
	First pass for the verlet method utilizing the proto_accel and 
	half_list method
	
	::param:: Tple of Particle objects
	'''
	A, B = pair
	proto = Proto_Acc(A, B)
	A_acc = proto * B.m
	B_acc =  proto * (-1.0)* A.m
	A.store_acc(A_acc)
	B.store_acc(B_acc)
	A.P = A.P + A.V  + A_acc*(1.0/2.0)
	B.P = B.P + B.V  + B_acc*(1.0/2.0)

def step_verlet_two(pair):
	'''
	First pass for the verlet method utilizing the proto_accel and 
	half_list method
	::param:: Tple of Particle objects
	'''
	A, B = pair
	proto = Proto_Acc(A, B)
	A_acc = proto * B.m
	B_acc = proto* (-1.0) * A.m
	A.V = (A.A + A_acc)*(1.0/2.0) 
	B.V = (B.A + A_acc)*(1.0/2.0)

