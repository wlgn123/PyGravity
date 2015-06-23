from Physics import Physics
import Data_IO

class PyGravity():
	def __init__(self):
		self.Physics = Physics()
		self.reader = None
		
	def set_reader(self, type):
		if type == 'CSV':
			self.reader = Data_IO.CSV_Reader()
		
	
