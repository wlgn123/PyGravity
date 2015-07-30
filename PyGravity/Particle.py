import numpy as np
'''
.. module:: Particle
   :platform: Unix
   :synopsis: Particles.

.. moduleauthor:: Russell Loewe <russloewe@gmail.com>

'''
class Particle(object):
	'''
	Class for creating a Particle object. Depends on Vectors.
	'''
	def __init__(self, name, P, V, m):
		'''
		Creates particle with initial valuse
		
		:param: name(string): Name of the particle. Used for keeping 
			track of particles when reading or writing to data files, or 
			printing to console.
		:param: P(Vector): Postitional vector of particle.
		:param: V(Vector): Velocity vector of particle.
		:param: m(Vector): Mass of the Particle. Represented as a 1 
			dimensional vector. 
		
		.. note:: Mass is represented as a 1D vector. A 1D vector is the 
			same as a scalar, but by using vector objects the abstraction 
			makes the code in the Physics Module a little bit more straight
			forward. It is possible to use a 2D or higher vector for mass 
			but unless new physics is discovered this won't make sense.
		
		.. note:: The unites are not specified. It is up to the calling 
			function to keep track of units.
		'''
		#check inputs
		assert type(P) is np.ndarray or list, 'Only numpy arrays, or lists are supported for Position Vector'
		assert type(V) is np.ndarray or list, 'Only numpy arrays, or lists are supported for Velocity Vector'
		
		if m is not float:
			try:
				m = float(m)
			except:
				raise TypeError("Particle mass couldn't be converted to float")
		
		self.P = np.array(P, dtype=float)    #particles position vector
		self.V = np.array(V, dtype=float)    #Particles velocity vector
		self.m = m        #particles mass
		self.name = name

	def move(self, timestep):
		'''
		Moves the particle based on the current velocity stored in 
		self.V by the specified time_step. Example
		
		.. code-block:: python
		
			>>> A_pos = Vector(['1', '1'])
			>>> A_veloc = Vector(['1', '2'])
			>>> A_mass = Vector(['1'])
			>>> A = Particle('A', A_pos, A_veloc, A_mass)
			>>> print A
			A: Position: (1,1), Velocity: (1,2), Mass: (1)
			>>> A.move(1)
			>>> print A
			A: Position: (2,3), Velocity: (1,2), Mass: (1)
			>>> A.move(2)
			>>> print A
			A: Position: (4,7), Velocity: (1,2), Mass: (1)
		
		:param: timestep(int): Increment of time to move by.
		'''
		new_pos = self.P + self.V*timestep
		self.P = new_pos

	def store_acc(self, acc):
		assert type(acc) is np.ndarray, "Only numpy arrays are supported for Acc Vectors"
		self.A = np.array(acc, dtype=float)
		
	def accelerate(self, A, timestep):
		'''
		Increase velocity by specified acceleration and timestep.
		
		Example using same particle from move() function:
		
		.. code-block:: python
		
			>>> print A
			A: Position: (1,1), Velocity: (1,2), Mass: (1)
			>>> A_acc = Vector(['1', '1'])
			>>> A.accelerate(A_acc, 1)
			>>> print A
			A: Position: (1,1), Velocity: (2,3), Mass: (1)
			>>> A.accelerate(A_acc, 2)
			A: Position: (1,1), Velocity: (4,5), Mass: (1)
		
		.. note:: The intention is that the timestep argument is defined
			globaly by the connecting module, and thus timestep for 
			accelerate() and timestep for move() should be the same.
		
		:param: A(Vector): Acceleration vector
		:param: timestep(int): Time increment.
		'''
		assert type(A) is np.ndarray, "Only numpy arrays are supported for Acc Vectors"
		new = self.V + np.array(A, dtype=float)*timestep
		self.V = new

	def __str__(self):
		particle_str = self.name + ': Position: ' + str(self.P) + ', Velocity: ' + str(self.V) + ', Mass: ' + str(self.m)
		return particle_str
		
	def round(self, n):
		'''
		Round each vector of the particle to sig digits. Wrapper for
		Vector.round()
		
		:param: n(int): Sig digits to round by.
		:returns: New particle with rounded attributes.
		
		.. code-block:: python
		
			>>> A = Particle('A', Vector([1.01]), Vector([1.02]), Vector([1.03]))
			>>> print A
			A: Position: (1.01), Velocity: (1.02), Mass: (1.03)
			>>> print A.round(1)
			A: Position: (1.0), Velocity: (1.0), Mass: (1.0)
		
		'''
		particle_str = self.name + ': Position: ' + str(self.P.round(n)) + ', Velocity: ' + str(self.V.round(n)) + ', Mass: ' + str(self.m.round(n))
		return particle_str

