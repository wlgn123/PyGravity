import unittest
from libs import round_sig, Vector, Particle, Physics
from math import log10, floor

class Round_test(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_rounding_domain(self):
        a = 0
        self.failUnless(round_sig(a, 1) == 0)
        
class Vector_Lib_tests(unittest.TestCase):
    def setUp(self):
        self.A = Vector(1,2,3)
        self.B = Vector(1,2,3)
        self.An = Vector(1.1, 2.2, 3.3)
        self.Bn = Vector(1.1, 2.2, 3.3)
        self.Aneg = Vector(-1, -2, -3)
        
    def test_Vector_Addition_integer(self):
        C = Vector.add(self.A, self.B)
        x = C.x
        y = C.y
        z = C.z
        self.failUnless(x == 2 )
        self.failUnless(y == 4 )
        self.failUnless(z == 6 )
        self.failIf(x == 20 )
        self.failIf(y == 40 )
        self.failIf(z == 60 )
        
    def test_Vector_Addition_real(self):
        C = Vector.add(self.An, self.Bn)
        x = C.x
        y = C.y
        z = C.z
        self.failUnless(x == 2.2 )
        self.failUnless(y == 4.4 )
        self.failUnless(z == 6.6 )
        
    def test_Vector_Addition_mixed(self):
        C = Vector.add(self.An, self.B)
        x = C.x
        y = C.y
        z = C.z
        self.failUnless(x == 2.1 )
        self.failUnless(y == 4.2 )
        self.failUnless(z == 6.3 )
        self.failIf(x == 2.2 )
        self.failIf(y == 4.1 )
        self.failIf(z == 6.4 )

    def test_Vector_Addition_negative(self):
        C = Vector.add(self.Aneg, self.B)
        x = C.x
        y = C.y
        z = C.z
        self.failUnless(x == 0 )
        self.failUnless(y == 0 )
        self.failUnless(z == 0 )
        
    def test_Vector_Addition_bignumber(self):
        BigA = Vector(1.3*10**12, 4.0*10**12, 6.3*10**13)
        BigB = Vector(1.1*10**12, 4.0*10**12, 6.1*10**13)
        C = Vector.add(BigA, BigB)
        x = C.x
        y = C.y
        z = C.z
        self.failUnless(x == 2.4*10**12 )
        self.failUnless(y == 8.0*10**12 )
        self.failUnless(z == 1.24*10**14 )
        self.failIf(x == 2.3*10**12 )
        self.failIf(y == 8.1*10**12 )
        self.failIf(z == 1.23*10**14 )
        
    def test_Vector_Addition_biger_number(self):
        BigA = Vector(1.3*10**24, 4.0*10**24, 6.3*10**13)
        BigB = Vector(1.1*10**24, 4.0*10**24, 6.1*10**13)
        Answer = Vector(2.4*10**24, 8.0*10**24, 1.24*10**14)
        C = Vector.add(BigA, BigB)
        self.failUnless(C.y == Answer.y)
        self.failUnless(C.y == Answer.y)
        self.failUnless(C.z == Answer.z)
        
    def test_Vector_scalar_multiplication_int(self):
        A = Vector(1,1,1)        
        C = Vector.times_scalar(2, A)
        Ans = Vector(2,2,2)
        self.failUnless(C.x == Ans.x)
        self.failUnless(C.y == Ans.y)
        self.failUnless(C.z == Ans.z)

    def test_Vector_scalar_multiplication_float(self):
        A = Vector(1.1, 2.1, 3.1)
        C = Vector.times_scalar(2.0, A)
        Ans = Vector(2.2,4.2,6.2)
        self.failUnless(C.x == Ans.x)
        self.failUnless(C.y == Ans.y)
        self.failUnless(C.z == Ans.z)
        self.failIf(C.z == Ans.x)
        self.failIf(C.x == Ans.y)
        self.failIf(C.y == Ans.z)
        
    def test_Vector_scalar_multiplication_neg(self):
        A = Vector(1.1, 1.2, -1)
        C = Vector.times_scalar(2.0, A)
        Ans = Vector(2.2,2.4,-2.0)
        self.failUnless(C.x == Ans.x)
        self.failUnless(C.y == Ans.y)
        self.failUnless(C.z == Ans.z)
        self.failIf(C.z == Ans.x)
        self.failIf(C.x == Ans.y)
        self.failIf(C.y == Ans.z)
        
    def test_Vector_scalar_multiple_big_numbers(self):
        A = Vector(2.0*10**20, 1.1*10**20, 4.2*10**20)
        a = 2.2*10**4
        C = Vector.times_scalar(a, A)
        Ans = Vector(4.4*10**24, 2.42*10**24, 9.24*10**24)
        print round_sig(Ans.z-C.z, 2)
       
        self.failUnless(round_sig(C.x,2) == round_sig(Ans.x, 2) )
        self.failUnless(round_sig(C.y,2) == round_sig(Ans.y, 2))
        self.failUnless(round_sig(C.z,2) == round_sig(Ans.z, 2))
        self.failIf(round_sig(C.z,2) == round_sig(Ans.x, 2) )
        self.failIf(round_sig(C.x,2) == round_sig(Ans.y, 2))
        self.failIf(round_sig(C.y,2) == round_sig(Ans.z, 2))
        
    def test_Vector_sub(self):
        A = Vector(1.1, 2.2, 3.3)
        B = Vector(1.1, 4.4, 1.1)
        C = Vector.sub(A, B)   
        Ans = Vector(0, -2.2, 2.2)
        self.failUnless(C.x == Ans.x)
        self.failUnless(C.y == Ans.y)
        self.failUnless(round_sig(C.z,2) == round_sig(Ans.z, 2))
        self.failIf(C.x == Ans.y)
        self.failIf(C.y == Ans.x)
        self.failIf(round_sig(C.z,2) == round_sig(Ans.x, 2))
        
    def test_vector_magnitude(self):
        A = Vector(3,4,0)
        self.failUnless(round_sig(Vector.magnitude(A), 2) == 5)
        self.failIf(round_sig(Vector.magnitude(A), 2) == 4)
        
        A = Vector(3.1*10**12,4.1*10**12,5.2*10**12)
        self.failUnless(round_sig(Vector.magnitude(A), 2) == 7.3*10**12)
        self.failIf(round_sig(Vector.magnitude(A), 2) == 7.2*10**12)
        
    def test_Vector_magnitude(self):
        A = Vector(10,10,10)
        C = Vector.unit(A)
        self.failUnless(round_sig(Vector.magnitude(C), 2) == 1)
        self.failUnless(round_sig(C.x, 3) == .577)
        self.failUnless(round_sig(C.y, 3) == .577)
        self.failUnless(round_sig(C.z, 3) == .577)
#need to test Vector.unit()
class Particle_Class_Tests(unittest.TestCase):
    def setUp(self):
       pass
       
    def test_particle_creation(self):
        a = Particle(Vector(1,2,3), Vector(1,1,1), 55.5)
        self.failUnless(hasattr(a, 'P'))
        self.failUnless(hasattr(a, 'V'))
        self.failUnless(hasattr(a, 'm'))
        
    def test_particle_motion(self):
        a = Particle(Vector(1,2,3), Vector(1,1,1), 55.5)
        a.move()
        V = Vector(1,1,1)
        P = Vector(2,3,4)
        self.failUnless(P.x == a.P.x)
        self.failUnless(P.y == a.P.y)
        self.failUnless(P.z == a.P.z)
        self.failIf(P.x == a.P.y)
        self.failIf(P.y == a.P.z)
        self.failIf(P.z == a.P.x)
        
    def test_particle_motion(self):
        a = Particle(Vector(1.1,2.1,3.0), Vector(1.1,2.1,3.0), 55.5)
        Accel = Vector(2,2,-4)
        Ans = Vector(3.1, 4.1, -1.0)
        a.accelerate(Accel)
        self.failUnless(Ans.x == a.V.x)
        self.failUnless(Ans.y == a.V.y)
        self.failUnless(Ans.z == a.V.z)
        self.failIf(Ans.x == a.V.z)
        self.failIf(Ans.y == a.V.x)
        self.failIf(Ans.z == a.V.y)
        
    def test_particle_acceleration(self):
        a = Particle(Vector(1, 1, 1), Vector(1,1,1), 44)
        Acc = Vector(3, 3, -1)
        V_ans = Vector(4, 4, 0)
        P_ans = Vector(5, 5, 1)
        a.accelerate(Acc)
        self.failUnless(V_ans.x == a.V.x)
        self.failUnless(V_ans.y == a.V.y)
        self.failUnless(V_ans.z == a.V.z)
        a.move()
        self.failUnless(P_ans.x == a.P.x)
        self.failUnless(P_ans.y == a.P.y)
        self.failUnless(P_ans.z == a.P.z)
        
class Physics_Class_Tests(unittest.TestCase):
    def setUp(self):
        self.part1 = Particle(Vector(1,1,1), Vector(1,1,1), 5)
        self.part2 = Particle(Vector(2*10**12,1*10**12,3*10**12), Vector(2.3, 1.2, 4.2), 5*10**6)
       
       
    def test_physics_particle_add(self):
        base = Physics()
        base.add_obj(self.part1)
        base.add_obj(self.part2)
        self.failUnless(self.part1 == base.objects[0])
        self.failIf(self.part1 == base.objects[1])
        self.failUnless(self.part2 == base.objects[1])
        self.failIf(self.part2 == base.objects[0])
    
    def test_Physics_Force_of_Gravity(self):
        part1 = Particle(Vector(1,1,1), Vector(1,1,1), 5)
        part2 = Particle(Vector(2,2,2), Vector(2.3, 1.2, 4.2), 10)
        answer = Vector(6.42*10**(-10), 6.42*10**(-10),6.42*10**(-10) )
        wrong_ans = Vector(1, 1, 1)
        base = Physics()
        force_vec = Physics.Fg(part1, part2)
        self.failUnless(force_vec)
        self.failUnless(round_sig(answer.x,2) == round_sig(force_vec.x, 2) )
        self.failUnless(round_sig(answer.y,2) == round_sig(force_vec.y, 2) )
        self.failUnless(round_sig(answer.z,2) == round_sig(force_vec.z, 2) )
        
        self.failIf(round_sig(wrong_ans.x,2) == round_sig(force_vec.x, 2) )
        self.failIf(round_sig(wrong_ans.y,2) == round_sig(force_vec.y, 2) )
        self.failIf(round_sig(wrong_ans.z,2) == round_sig(force_vec.z, 2) )
        
def main():
	unittest.main()

if __name__ == "__main__":
	main()
