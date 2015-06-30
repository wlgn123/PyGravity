from Physics import Physics
import Data_IO
##
#@author Russell Loewe russloewe@gmail.com
#@file PyGravity.py
#@date 6-28-2015
#@brief main entry point for PyGravty module
#cantains the base class to tie together the sub modules of 
#PyGravity

class PyGravity():
    ##
    #@brief init
    # initial vector dimension set to 3
    def __init__(self):
        self.dimension = 3
        self.Physics = Physics()
        self.reader = Data_IO.Reader()
        self.writer = Data_IO.Writer()

		##
        #@brief override vector dimsion 
        #changes the vector dimsion for the csv reader parser
        #@see Data_IO.Reader
    def set_dimension(self, dim):
        self.Physics.dimension = dim
        self.reader.dimension = dim
		
    def read_file(self, file_name):
        self.reader.read_file(file_name)
        self.Physics.objects = self.reader.objects
        
    def write_file(self, name):
        self.writer.objects = self.Physics.objects
        self.writer.write_file(name)
	
