import unittest
from PyGravity import round_sig, Vector, Particle, Physics
from decimal import *


class Physics_Class_Tests(unittest.TestCase):
	def setUp(self):
		self.part1 = Particle('a',Vector([1,1,1]), Vector([1,1,1]), Vector([5]))
		self.part2 = Particle('b',Vector([2*10**42,1*10**42,3*10**42]), Vector([2.3, 1.2, 4.2]), Vector([5*10**6]))



	def _test_physics_particil_add(self):
		base = Physics()
		base.add_obj(self.part1)
		base.add_obj(self.part2)
		self.failUnless(np.allclose(self.part1, base.objects[0]) )
		self.failUnless(np.allclose(self.part2, base.objects[1]) )

	def test_Physics_Force_of_Gravity(self):
		part1 = Particle('a',Vector([1,1,1]), Vector([1,1,1]), Vector([5]))
		part2 = Particle('b',Vector([2,2,2]), Vector([2.3, 1.2, 4.2]), Vector([10]))
		answer = Vector([-6.42e-10, -6.42e-10,-6.42e-10 ])
		wrong_ans = Vector([1, 1, 1])
		base = Physics()
		force_vec = base.Fg(part1, part2)
		self.failUnless(answer.round(2) == force_vec.round(2) )


	def _test_Physics_force_gravity_summation_for_one_particle(self):
		A = Particle('A',Vector(1.00,1.00,1.00), Vector(0,0,0), 10)
		B = Particle('B',Vector(2.00,2.00,2.00), Vector(0,0,0), 10)
		C = Particle('C',Vector(3.00,3.00,3.00), Vector(0,0,0), 10)
		D = Particle('D',Vector(4.00,4.00,4.00), Vector(0,0,0), 10)
		base = Physics()
		base.add_obj(A)
		base.add_obj(B)
		base.add_obj(C)
		base.add_obj(D)

		f = base.sum_Fg_one_particle(base.objects[0])
		self.failUnless(round_sig(f.x, 3 ) == round_sig(1.75*10**(-9), 3))
		self.failUnless(round_sig(f.y, 3 ) == round_sig(1.75*10**(-9), 3))
		self.failUnless(round_sig(f.z, 3 ) == round_sig(1.75*10**(-9), 3))

	def _test_partitcle_acceleration_3_object_harmonic_range(self):
		#this test setups 3 particles. one tiny, spaced eqidistance above the line of two
		#very heavy objects. The particle is supposed to bounce up and down across the line the
		# two heavy objects set on. This is testing to make sure the particle stays between
		# a maxima and minima and doesn't fly off in either direction.
		A = Particle('A',Vector(0,10.00,0), Vector(0,0,0), 1)
		B = Particle('B',Vector(-10,0,0), Vector(0,0,0), 10000000000)
		C = Particle('C',Vector(10,0,0), Vector(0,0,0), 10000000000)

		base = Physics()
		base.add_obj(A)
		base.add_obj(B)
		base.add_obj(C)
		for i in range(1000):
			base.apply_gravitational_acceleration(base.objects[0])
			base.objects[0].move
			self.failIf(base.objects[0].P.y > 12)
			self.failIf(base.objects[0].P.y < (-12))

			self.failUnless(base.objects[0].P.y < 12)
			self.failUnless(base.objects[0].P.y > (-12))



def test_physics():
	unittest.main()

if __name__ == "__main__":
	test_physics()
