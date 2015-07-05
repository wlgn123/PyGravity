
import unittest
from PyGravity import round_sig, Vector, Particle

from decimal import *


class Particle_Class_Tests(unittest.TestCase):
	def setUp(self):
		pass

	def test_particle_creation(self):
		a = Particle('a',Vector([1,2,3]), Vector([1,1,1]), Vector([55.5]))
		self.failUnless(hasattr(a, 'P'))
		self.failUnless(hasattr(a, 'V'))
		self.failUnless(hasattr(a, 'm'))
		self.failUnless(a.name == 'a')

	def test_particle_motion(self):
		a = Particle('a', Vector([1,2,3]), Vector([1,1,1]), Vector([55.5]))
		a.move(1)
		V = Vector([1,1,1])
		P = Vector([2,3,4])
		self.failUnless(P== a.P)

	def test_particle_motion2(self):
		a = Particle('a',Vector([1.1,2.1,3.0]), Vector([1.1,2.1,3.0]), Vector([55.5]))
		Accel = Vector([2,2,-4])
		Ans = Vector([3.1, 4.1, -1.0])
		a.accelerate(Accel,1)
		self.failUnless(Ans == a.V)

	def test_particle_acceleration(self):
		a = Particle('a',Vector([1, 1, 1]), Vector([1,1,1]), Vector([44]))
		Acc = Vector([3, 3, -1])
		V_ans = Vector([4, 4, 0])
		P_ans = Vector([5, 5, 1])
		a.accelerate(Acc,1)
		self.failUnless(V_ans == a.V)
		a.move(1)
		self.failUnless(P_ans == a.P)


def test_particle():
	unittest.main()

if __name__ == "__main__":
	test_particle()
