import unittest
from libs import Vector
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
       
        self.failUnless(C.x == Ans.x )
        self.failUnless(round_sig(C.y,2)-round_sig(Ans.y, 2) == 0)
        self.failUnless(round_sig(C.z,2)-round_sig(Ans.z, 2) == 0)

def main():
	unittest.main()

if __name__ == "__main__":
	main()
