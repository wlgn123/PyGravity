import unittest
from libs import Vector



class Vector_Lib_tests(unittest.TestCase):
    def setUp(self):
        self.A = Vector(1,2,3)
        self.B = Vector(1,2,3)
        self.An = Vector(1.1, 2.2, 3.3)
        self.Bn = Vector(1.1, 2.2, 3.3)
        self.Aneg = Vector(-1, -2, -3)
        
    def test_Vector_Addition_integer(self):
        C = self.A.add(self.B)
        x = C.x
        y = C.y
        z = C.z
        self.failUnless(x == 2 )
        self.failUnless(y == 4 )
        self.failUnless(z == 6 )
        
    def test_Vector_Addition_real(self):
        C = self.An.add(self.Bn)
        x = C.x
        y = C.y
        z = C.z
        self.failUnless(x == 2.2 )
        self.failUnless(y == 4.4 )
        self.failUnless(z == 6.6 )
        
    def test_Vector_Addition_mixed(self):
        C = self.An.add(self.B)
        x = C.x
        y = C.y
        z = C.z
        self.failUnless(x == 2.1 )
        self.failUnless(y == 4.2 )
        self.failUnless(z == 6.3 )

    def test_Vector_Addition_negative(self):
        C = self.Aneg.add(self.B)
        x = C.x
        y = C.y
        z = C.z
        self.failUnless(x == 0 )
        self.failUnless(y == 0 )
        self.failUnless(z == 0 )
        
    def test_Vector_Addition_bignumber(self):
        BigA = Vector(1.3*10**12, 4.0*10**12, 6.3*10**13)
        BigB = Vector(1.1*10**12, 4.0*10**12, 6.1*10**13)
        C = BigA.add(BigB)
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
        C = BigA.add(BigB)
        self.failUnless(C.y == Answer.y)
        self.failUnless(C.y == Answer.y)
        self.failUnless(C.z == Answer.z)


def main():
	unittest.main()

if __name__ == "__main__":
	main()
