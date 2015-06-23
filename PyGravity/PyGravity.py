from Physics import Physics
import Data_IO

class PyGravity():
	def __init__(self):
		self.dimension = 3
		self.Physics = Physics()
		self.reader = Data_IO.Reader()
		self.objects = []
		
	def set_reader_type(self, r_type):
		self.reader.dimension = self.dimension
		self.reader.set_reader_type(r_type)
		
	def set_dimension(self, dim):
		self.Physics.dimension = dim
		
	def read_file(self, file_name):
		self.objects = self.reader.read_file(file_name)
	
			
	
