from Physics import Physics
import Data_IO
##
#@author Russell Loewe russloewe@gmail.com
#@file ./PyGravity/PyGravity.py
#@date 6-28-2015
#@brief main entry point for PyGravty module
#cantains the base class to tie together the sub modules of 
#PyGravity

class PyGravity():

	def __init__(self):
		self.dimension = 3
		self.Physics = Physics()
		self.reader = Data_IO.Reader()
		self.writer = Data_IO.Writer()
		##
		#@brief init
		# initial vector dimension set to 3

	def set_dimension(self, dim):
		self.Physics.dimension = dim
		self.reader.dimension = dim
		##
		#@brief override vector dimsion 
		#changes the vector dimsion for the csv reader parser
		#@see Data_IO.Reader


	def read_file(self, file_name):
		self.reader.read_file(file_name)
		self.Physics.objects = self.reader.objects
		##
		#@brief use to load a set of particels from a CSV file
		# @param file_name
		# Use to load a set of particles from a CSV data file. 
		# The particles are then loaded into the objects list
		# under Physics.objects.
		#@see PyGravity.dimension
		#
		#@note the dimension of the PyGravity must match the dimension
		#of the particles in the CSV file
		#@see Data_IO.Reader.dimension

	def write_file(self, file_name):
		self.writer.objects = self.Physics.objects
		self.writer.write_file(file_name)
		##
		#@brief Write the current object set to an output file
		#@param file_name name of output file, will be created if 
		#non-existant
		#@see Data_IO.Writer

