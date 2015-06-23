import csv

class Reader(object):
	def __init__(self, path, physics):
		self.path = path
		self.data = []
		
	def read_file(self):		
		with open(self.path, 'rb') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=':', quotechar='|')
			for row in spamreader:
				try:
					if self.dimension == 3:
						self.add_obj(Particle(row[0], Vector(row[1:4]), Vector(row[4:7]), Vector(row[7:]) ) )
					elif self.dimension == 2:
						self.add_obj(Particle(row[0], Vector(row[1:3]), Vector(row[3:5]), Vector(row[5:]) ) )
				except ValueError as e:
					print e
