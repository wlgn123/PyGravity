from Physics import Physics
import Data_IO

class PyGravity():
	def __init__(self):
		self.dimension = 3
		self.Physics = Physics()
		self.reader = Data_IO.Reader()

		
	def set_dimension(self, dim):
		self.Physics.dimension = dim
		self.reader.dimension = dim
		
	def read_file(self, file_name):
		self.reader.read_file(file_name)
		self.Physics.objects = self.reader.objects
	
			
	
