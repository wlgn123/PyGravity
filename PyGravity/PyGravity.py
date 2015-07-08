import Physics
import Global_Container
import Data_IO
import decimal
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
		self.values = Global_Container.Global_Container()
		self.reader = Data_IO.Reader()
		self.writer = Data_IO.Writer()


	def set_dimension(self, dim):
		'''Set global dimension
		
		Dimension is defaulted to 3, but can be overriden here
		
		.. code-block:: python
		
			PyGravity.set_dimension(4)
		
		:param: (int) The diminsion of the vectors

		'''
		self.values.set_prec()

	def set_precision(self, prec):
		'''
		Set the global precision. Default is 200.
		
		:param: prec(int) New global precision
		'''
		self.values.precision = prec
		decimal.getcontext().prec = self.values.precision



	def read_file(self, file_name):
		''' 
		Use to load a set of particles from a CSV data file, 
		The particles are then loaded into the objects list
		under Physics.objects.
		 
		:param: file_name(string) Name of data file to be read.
		
		
		:py:func:'PyGravity.set_dimension'
		
		.. note::
			the dimension of the PyGravity.dimension must match the 
			the dimension of the particles in the CSV file.
		
		.. todo:: figure out sphinx references
		
		'''
		self.reader.read_file(file_name)
		for item in self.reader.objects:
			self.values.add_particle(item)


	def write_file(self, file_name):
		'''
		Write current particle set to output file
		
		:param: (string)file_name File name and path to write current
			dataset
		
		'''
		self.writer.objects = self.values.particle_list
		self.writer.write_file(file_name)

