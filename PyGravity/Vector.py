from round_sig import round_sig
from decimal import *
'''
.. module:: Vector
   :platform: Unix
   :synopsis: Vector Mod

.. moduleauthor:: Russell Loewe <russloewe@gmail.com>

'''



class Vector(object):
	'''
	Vector class for creating a vector object
	
	If A, and B are vectors then the following operations are supported:
	
	.. code-block:: python
	
		A + B
		A - B
		print A
		A == B
		A[1]
		A * 2
	
	.. note:: The scalar multiplication is supported by A*2, however
		2*A is not supported.
	'''
	def __init__(self, array):
		'''
		The vector object is intialized with an array 
		containing the values for the vector. The length of the 
		array is arbitrary, thus vectors of any dimension can easily 
		be created. For example a vector of 3 dimensions is created 
		by 
		
		.. code-block:: python
		
			A = Vector(['1','2','3'])
		
		and a vector of 6 dimensions is created by 
		
		.. code-block:: python
		
			B = Vector(['1','2','3','4','5','6']).
		
		.. note::
			To ensure accuracy use strings not floats. As in ['1.1', '2.1'].
			The vector uses Decimal objects for accuracy. Decimal will
			convert strings to Decimal objects without loss of accuracy, 
			but floats will suffer rounding errors before being converted 
			to Decimal objects.
		
		'''
		self.vector = self.makedecimal(array)

	def __str__(self):
		string = '('
		c = 0
		for item in self.vector:
			if c!=0:
				string = string + ',' + str(item)
			else:
				string = string  + str(item)
			c += 1
		string = string + ')'

		return string

	def __add__(self, other_vector):
		if self.array_mismatch(other_vector):
			raise ValueError('vector dimension doesnt match')

		new_array = []
		for index, val in enumerate(self.vector):
			new_array.append(val + other_vector.vector[index])
		return Vector(new_array)

	def __radd__(self, other_vector):
		if self.array_mismatch(other_vector):
			raise ValueError('vector dimension doesnt match')
			
		new_array = []
		for index, val in enumerate(self.vector):
			new_array.append(val + other_vector.vector[index])

		return Vector(new_array)

	def __sub__(self, other_vector):
		new_array = []
		for index, val in enumerate(self.vector):
			new_array.append(val - other_vector.vector[index])
		return Vector(new_array)

	def __rsub__(self, other_vector):
		new_array = []
		for index, val in enumerate(self.vector):
			new_array.append(val - other_vector.vector[index])
		return Vector(new_array)

	def __eq__(self, other_vector):
		if self.array_mismatch(other_vector):
			raise ValueError('vector dimension doesnt match')
		for element in self.vector:
			try:
				if element != other_vector.vector[i]:
					return False
			except Exception:
				return False
			i += 1
		return True

	def makedecimal(self, array):
		new_array = []
		for val in array:
			new_array.append(Decimal(str(val)))
		return new_array

	def array_mismatch(self, other):
		'''
		Checks dimension of current vector against another vector.
		For example, for two vectors A and B, A.array_mismatch(B)
		checks A against B. Example:
		
		.. code-block:: python
		
			>>>A = Vector(['1','2'])
			>>>B = Vector(['3', '4', '5'])
			>>>C = Vector(['9', '7'])
			
			>>>A.array_mismatch(B)
			True
			>>>A.array_mistmatch(C)
			False
		
		:returns: True if the two Vectors are of different size, False 
			if they are the same size
		'''
		if len(self.vector) != len(other.vector) :
			return True
		else:
			return False

	def __mul__(self, scalar):
		new_array = []
		for item in self.vector:
			new_array.append(item * Decimal(scalar))
		return Vector(new_array)

	def __getitem__(self,index):
		return self.vector[index]


	def round(self, a):
		'''
		Rounds the indiviedule components to 'a' sig digits.
		
		:param: a(int): noumber of sig digits to round to
		:returns: Vector
		
		.. note::
			Only rounds up to 10 sig digits untill the underlaying, 
			round_sig function is fixed
		'''
		i = int(round_sig(a,1))
		new = []
		for item in self.vector:
			new.append(round_sig(item, i))
		return Vector(new)

	def magnitude(self):
		'''
		Find the magnitude of the current vector using Pythagorean theorem.
		This is independant of the dimension of the vector and will find the 
		megnitude for any vector.
		
		:returns: magniutude as a Decimal object.
		
		'''
		total = 0
		for item in self.vector:
			total += item**2
		return total.sqrt()


	def unit(self):
		'''
		Normalize Vector
		
		:returns: New Vector that is the unit vector of the original.
		
		.. code-block:: python
		
			>>> A = Vector(['1', '2'])
			>>> print A
			(1,2)
			>>> print A.unit()
			(0.4472135954999579392818347337,0.8944271909999158785636694674)

			
		'''
		return self * (1/ self.magnitude())






