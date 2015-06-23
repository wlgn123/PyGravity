import csv
from Particle import Particle
from Vector import Vector

class Reader(object):
	def __init__(self):
		self.objects = []
		self.dimension = 3
		self.data_type = None
	
	def set_reader_type(self, type):
		if type == 'CSV':
			self.data_type = 1
			
	def read_file(self, path):
		if self.data_type == 1:
			self.CSV_Reader(path)
		
	def CSV_Reader(self, path):		
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
		for item in self.objects:
			if obj.name == item.name:
				raise ValueError("duplicate name found, not adding last entry")
				return
		self.objects.append(obj)
