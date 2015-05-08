import unittest
from libs import Vector, Particle
from math import log10, floor

def round_sig(x, sig=2):
   return round(x, sig-int(floor(log10(x)))-1)


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
        A = Vector(1.1, 1.1, 1.1)
        C = Vector.times_scalar(2.0, A)
        Ans = Vector(2.2,2.2,2.2)
        self.failUnless(C.x == Ans.x)
        self.failUnless(C.y == Ans.y)
        self.failUnless(C.z == Ans.z)
        
    def test_Vector_scalar_multiplication_neg(self):
        A = Vector(1.1, 1.2, -1)
        C = Vector.times_scalar(2.0, A)
        Ans = Vector(2.2,2.4,-2.0)
        self.failUnless(C.x == Ans.x)
        self.failUnless(C.y == Ans.y)
        self.failUnless(C.z == Ans.z)
        
    def test_Vector_scalar_multiple_big_numbers(self):
        A = Vector(2.0*10**20, 1.1*10**20, 4.2*10**20)
        a = 2.2*10**4
        C = Vector.times_scalar(a, A)
        Ans = Vector(4.4*10**24, 2.42*10**24, 9.24*10**24)
        print round_sig(Ans.z-C.z, 2)
       
        self.failUnless(round_sig(C.x,2) == round_sig(Ans.x, 2) )
        self.failUnless(round_sig(C.y,2) == round_sig(Ans.y, 2))
        self.failUnless(round_sig(C.z,2) == round_sig(Ans.z, 2))
        
    def test_Vector_sub(self):
        A = Vector(1.1, 2.2, 3.3)
        B = Vector(1.1, 4.4, 1.1)
        C = Vector.sub(A, B)   
        Ans = Vector(0, -2.2, 2.2)
        self.failUnless(C.x == Ans.x)
        self.failUnless(C.y == Ans.y)
        self.failUnless(round_sig(C.z,2) == round_sig(Ans.z, 2))
        
    def test_vector_magnitude(self):
        A = Vector(3,4,0)
        self.failUnless(round_sig(Vector.magnitude(A), 2) == 5)
        
        A = Vector(3.1*10**12,4.1*10**12,5.2*10**12)
        self.failUnless(round_sig(Vector.magnitude(A), 2) == 7.3*10**12)
        
    def test_Vector_magnitude(self):
        A = Vector(10,10,10)
        C = Vector.unit(A)
        self.failUnless(round_sig(Vector.magnitude(C), 2) == 1)
        self.failUnless(round_sig(C.x, 3) == .577)
        self.failUnless(round_sig(C.y, 3) == .577)
        self.failUnless(round_sig(C.z, 3) == .577)

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
        
    def test_particle_motion(self):
        a = Particle(Vector(1.1,2.1,3.0), Vector(1.1,2.1,3.0), 55.5)
        Accel = Vector(2,2,-4)
        Ans = Vector(3.1, 4.1, -1.0)
        a.accelerate(Accel)
        self.failUnless(Ans.x == a.V.x)
        self.failUnless(Ans.y == a.V.y)
        self.failUnless(Ans.z == a.V.z)
        
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
        
        
        
def main():
	unittest.main()

if __name__ == "__main__":
	main()
