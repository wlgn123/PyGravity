import csv
from Particle import Particle
from Vector import Vector
'''
.. module:: Data_IO
   :platform: Unix
   :synopsis: data imput output

.. moduleauthor:: Russell Loewe <russloewe@gmail.com>

'''
class Reader(object):
	'''Data reading and writing class.

	'''
	def __init__(self):
		'''
		:attr: objects (list)
		:attr: dimension (int)
		.. note::
			Reader.object is init as empty. The calling function must
			provide a reference to the global object list.
		'''
		self.objects = [] 
		self.dimension = 3
		

			
	def read_file(self, path):
		'''
		Read a dataset from a file. Will detect the format 
		of the data file. Currently only CSV is supported, so only
		.csv files are execpted. Later when other formates are included
		this will be where the correct parser is chosen.
		
		:param: path(string) File name and path of data file. Example, 
			'./data.csv', or '/home/russ/data/set1.csv'
		
		:raises: ValueError for incompatible file types
		'''
		file_type = path.split('.')[-1]
		
		if file_type == 'csv':
			self.CSV_Reader(path)
		else:
			raise ValueError('File type not supported')
			return
		
	def CSV_Reader(self, path):
		'''
		Reads from a CSV file and parses the the values into particle 
		objects from the PyGravity.Particle module
		
		:param: path(string) Name and path to the data file. Either 
			relative or absolute path
		
		'''
		with open(path, 'rb') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=':', quotechar='|')
			for row in spamreader:
				try:
					if self.dimension == 3:
						self.add_obj(Particle(row[0], Vector(row[1:4]), Vector(row[4:7]), Vector(row[7:]) ) )
					elif self.dimension == 2:
						self.add_obj(Particle(row[0], Vector(row[1:3]), Vector(row[3:5]), Vector(row[5:]) ) )
				except ValueError as e:
					print e
					
	def add_obj(self, obj):
		'''
		Once a line from the data file is parsed and loaded into a 
		partilce object, this function adds the particle to the given
		list of objects. The list of objects is provided by the parent 
		function.
		
		:param: obj(PyGravity.Particle) Particle to be added to global 
			list
		'''
		for item in self.objects:
			if obj.name == item.name:
				raise ValueError("duplicate name found, not adding last entry")
				return
		self.objects.append(obj)

class Writer(object):
	'''
	Class to create a Writer object
	'''
	
	def __init__(self):
		'''
		:attr: objects (list)
		'''
		self.objects = []
		
	def write_file(self, file_name):
		'''
		Write current global dataset in objects list to 
		a CSV file
		
		:param: file_name(string) Name and path for output file.
		
		.. note:: Output file will be created if it's not already on 
			the disk
		'''
		with open(file_name, 'w+') as f:
			for object in self.objects:
				f.write(self.object_to_string(object))
				
	def object_to_string(self, ob):
		'''
		Takes a particle object and formates it to a CSV string for file
		output
		
		:param: ob(PyGravity.Particle) Particle object to be formated 
		:returns: Formatted string 
		'''
		string = str(ob.name) + ':' 
		for item in ob.P:
			string = string + str(item) +':'
		for item in ob.V:
			string = string + str(item) + ':'
		string = string + str(ob.m[0])+'\n'
		return string
