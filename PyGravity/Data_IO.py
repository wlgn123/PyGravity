import csv
import xml.etree.ElementTree as ET
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
	
	
	.. todo:: Change date format for easy continuation of simulations. 
		add timestamp along with other particle attribute.
	
	.. todo:: XML writer
	
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
		of the data file. Currently only CSV and XML is supported, so only
		.csv or .xml files are execpted. Later when other formates are included
		this will be where the correct parser is chosen.
		
		:param: path(string) File name and path of data file. Example, 
			'./data.csv', or '/home/russ/data/set1.xml'
		
		:raises: ValueError for incompatible file types
		'''
		file_type = path.split('.')[-1]
		
		if file_type == 'csv':
			self.CSV_Reader(path)
		elif file_type == 'xml':
			self.XML_Reader(path)
		else:
			raise ValueError('File type not supported')
			return
		
	def CSV_Reader(self, path):
		'''
		Reads from a CSV file and parses the the values into particle 
		objects from the PyGravity.Particle module
		
		:param: path(string) Name and path to the data file. Either 
			relative or absolute path
			
		.. note:: Vector dimension needs to be given to the reader beforehand.
		
		'''
		with open(path, 'rb') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=':', quotechar='|')
			for row in spamreader:
				try:
					if self.dimension == 3:
						self.add_obj(Particle(row[0],
									 row[1:4],
									 row[4:7],
									 float(str(row[7]) )))
					elif self.dimension == 2:
						self.add_obj(Particle(row[0],
									 row[1:3],
									 row[3:5],
									 float(str(row[5]) ) ))
				except ValueError as e:
					print e
					
	def XML_Reader(self, path):
		'''
		XML Reader. Will read an xml data file and load the particles
		into the self.objects list for the PyGravity base to later 
		unload.
		
		:param: path(string): Path to xml file. 
		
		.. note:: This parser does not need to know the dimension for the
			vectors. It passes the vector strings straight into the Vector
			object as-is.
			
		.. todo:: Error handling for parser
		'''
		tree = ET.parse(path)
		root = tree.getroot()
		for particle in root.iter('particle'):
			
			for item in particle:
				if item.tag == 'name':
					name = item.text
				if item.tag == 'position':
					position = item.text
				if item.tag == 'velocity':
					velocity = item.text
				if item.tag == 'mass':
					mass = item.text
			new_part = Particle(name, 
								position.split(';'),
								velocity.split(';'), 
								mass )
			self.add_obj(new_part)

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
		
		.. todo:: need better way of makeing objects into strings:
		'''
		string = ob.name + ':' 
		for item in ob.P:
			string = string + str(item) +':'
		for item in ob.V:
			string = string + str(item) + ':'
		string = string + str(ob.m[0])+'\n'
		return string
