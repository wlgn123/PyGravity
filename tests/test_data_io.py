import unittest
from PyGravity import round_sig, Vector, Particle, Physics, Data_IO
from decimal import *


class Data_io_Class_Tests(unittest.TestCase):
	def setUp(self):
		pass
		
	def test_read_csv(self):
		a = Particle('a', Vector(['1.1','1.2','0']), Vector(['0','0','0']), Vector(['50']))
		d = Particle('d', Vector(['2.1','2.1','0']), Vector(['0','0','0']), Vector(['20']))
		base = Data_IO.Reader()
		base.read_file('./test_data.csv')
		self.failUnless(base.objects[0].name == a.name)
		self.failUnless(base.objects[0].P == a.P)
		self.failUnless(base.objects[0].V == a.V)
		self.failUnless(base.objects[0].m == a.m)



def test_data_io():
	unittest.main()

if __name__ == "__main__":
	test_data_io()

