import unittest
from libs import round_sig, Vector, Particle, Physics
import numpy as np
from math import log10, floor
from decimal import *

class Round_test(unittest.TestCase):
    def setUp(self):
        pass

    def test_rounding_domain(self):
        a = 0
        self.failUnless(round_sig(a, 1) == 0)

    def test_neg_numbers(self):
        a = -1.2
        self.failUnless(round_sig(a,2) == -1.2)


class Vector_Class_Tests(unittest.TestCase):
    def setUp(self):
       self.A = Vector([1,2,3])
       self.B = Vector([1,1,1])
       self.C = Vector([2.334e+20, 3.123456e+20])
       self.D = Vector([4.334e+20, 2.123456e+20])
       self.E = Vector(['1.2131313131231231231231231231231231231123123123123', '2.213123123123131231231312312312312312123'])
       self.F = Vector(['1.2131313131231231231231231231231231231123123123121', '2.213123123123131231231312312312312312121'])
       self.H = Vector(['1.00000000000000000000000000000000000000000000000001','0'])
       self.I = Vector(['1.00000000000000000000000000000000000000000000000002','0'])
       self.L = Vector(['1.1111111111111111111111111111111111111222'])
       self.M = Vector(['1.2345679133333333333333333333333333333456543211084'])

       self.Z = Vector([0,0])

    def test_equalities(self):
        self.failUnless(self.A == self.A)
        self.failUnless((self.B + self.A) == (self.B + self.A))
        self.failIf(self.A == self.B)


    def test_array_match(self):
        self.failIf(self.E.array_mismatch(self.F))
        self.failUnless(self.F.array_mismatch(Vector(['1'])))

    def test_more_addition(self):
        self.failUnless((self.E+self.F) == (self.E+self.F))

    def test_big_equalities(self):
        self.failUnless(self.C == self.C)
        self.failIf(self.C == self.D)

    def test_equality_precise(self):
        self.failUnless(self.E == self.E)
        self.failIf(self.E == self.A)
        self.failIf(( self.E- self.F) == self.Z)
        self.failUnless(self.I - self.I  == self.Z)
        self.failIf(self.H + self.H == self.H + self.I)

    def test_scalar_mul(self):
        self.failUnless(self.L*Decimal('1.111111122') == self.M)


class Particle_Class_Tests(unittest.TestCase):
    def setUp(self):
       pass

    def test_particle_creation(self):
        a = Particle(np.array([1,2,3]), np.array([1,1,1]), 55.5)
        self.failUnless(hasattr(a, 'P'))
        self.failUnless(hasattr(a, 'V'))
        self.failUnless(hasattr(a, 'm'))

    def test_particle_motion(self):
        a = Particle(np.array([1,2,3]), np.array([1,1,1]), 55.5)
        a.move()
        V = np.array([1,1,1])
        P = np.array([2,3,4])
        self.failUnless(np.allclose(P, a.P))

    def test_particle_motion2(self):
        a = Particle(np.array([1.1,2.1,3.0]), np.array([1.1,2.1,3.0]), 55.5)
        Accel = np.array([2,2,-4])
        Ans = np.array([3.1, 4.1, -1.0])
        a.accelerate(Accel)
        self.failUnless(np.allclose(Ans, a.V))

    def test_particle_acceleration(self):
        a = Particle(np.array([1, 1, 1]), np.array([1,1,1]), 44)
        Acc = np.array([3, 3, -1])
        V_ans = np.array([4, 4, 0])
        P_ans = np.array([5, 5, 1])
        a.accelerate(Acc)
        self.failUnless(np.allclose(V_ans, a.V))
        a.move()
        self.failUnless(np.allclose(P_ans, a.P))

class Physics_Class_Tests(unittest.TestCase):
    def setUp(self):
        self.part1 = Particle(np.array([1,1,1]), np.array([1,1,1]), 5)
        self.part2 = Particle(np.array([2*10**42,1*10**42,3*10**42]), np.array([2.3, 1.2, 4.2]), 5*10**6)


    def _test_physics_particle_add(self):
        base = Physics()
        base.add_obj(self.part1)
        base.add_obj(self.part2)
        self.failUnless(np.allclose(self.part1, base.objects[0]) )
        self.failUnless(np.allclose(self.part2, base.objects[1]) )

    def test_Physics_Force_of_Gravity(self):
        part1 = Particle(np.array([1,1,1]), np.array([1,1,1]), 5)
        part2 = Particle(np.array([2,2,2]), np.array([2.3, 1.2, 4.2]), 10)
        answer = np.array([-6.42*10**(-10), -6.42*10**(-10),-6.42*10**(-10) ])
        wrong_ans = np.array([1, 1, 1])
        base = Physics()
        force_vec = Physics.Fg(part1, part2)
        self.failUnless(np.allclose(answer, force_vec) )


    def _test_Physics_force_gravity_summation_for_one_particle(self):
        A = Particle(Vector(1.00,1.00,1.00), Vector(0,0,0), 10)
        B = Particle(Vector(2.00,2.00,2.00), Vector(0,0,0), 10)
        C = Particle(Vector(3.00,3.00,3.00), Vector(0,0,0), 10)
        D = Particle(Vector(4.00,4.00,4.00), Vector(0,0,0), 10)
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
        A = Particle(Vector(0,10.00,0), Vector(0,0,0), 1)
        B = Particle(Vector(-10,0,0), Vector(0,0,0), 10000000000)
        C = Particle(Vector(10,0,0), Vector(0,0,0), 10000000000)

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



def main():
	unittest.main()

if __name__ == "__main__":
	main()
