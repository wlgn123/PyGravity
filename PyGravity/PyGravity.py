from Physics import Physics
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
		self.dimension = 3
		self.Physics = Physics()
		self.reader = Data_IO.Reader()
		self.writer = Data_IO.Writer()


	def set_dimension(self, dim):
		'''Set global dimnsion
		

		Dimension is defaulted to 3, but can be overriden here

		Args:
			arg1 (int): The diminsion of the 
		'''
		self.Physics.dimension = dim
		self.reader.dimension = dim



	def read_file(self, file_name):
		''' Use to load a set of particels from a CSV file
		
		Use to load a set of particles from a CSV data file, 
		 The particles are then loaded into the objects list
		 under Physics.objects.
		 
		:param: (string)file_name Name of data file to be read
		

		:py:func:'PyGravity.set_dimension'
		
		.. note::
			the dimension of the PyGravity.dimension must match the 
			the dimension of the particles in the CSV file.
			
		see :py:class:'PyGravity.Data_IO'
		
		'''
		self.reader.read_file(file_name)
		self.Physics.objects = self.reader.objects


	def write_file(self, file_name):
		self.writer.objects = self.Physics.objects
		self.writer.write_file(file_name)
		##
		#@brief Write the current object set to an output file
		#@param file_name name of output file, will be created if 
		#non-existant
		#@see Data_IO.Writer

