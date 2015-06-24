import csv
from Particle import Particle
from Vector import Vector

class Reader(object):
	def __init__(self):
		self.objects = []
		self.dimension = 3

			
	def read_file(self, path):
		file_type = path.split('.')[-1]
		
		if file_type == 'csv':
			self.CSV_Reader(path)
		else:
			raise ValueError('File type not supported')
			return
		
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

class Writer(object):
    def __init__(self):
        self.objects = []
        
    def write_file(self, file_name):
        with open(file_name, 'w+') as f:
            for object in self.objects:
                f.write(self.object_to_string(object))
                
    def object_to_string(self, ob):
        string = str(ob.name) + ':' 
        for item in ob.P:
            string = string + str(item) +':'
        for item in ob.V:
            string = string + str(item) + ':'
        string = string + str(ob.m[0])+'\n'
        return string
