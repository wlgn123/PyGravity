import unittest
from libs import Vector



class Local_files_tests(unittest.TestCase):
    def setUp(self):
        self.A = Vector(1,2,3)
        self.B = Vector(1,2,3)
        self.An = Vector(1.1, 2.2, 3.3)
        self.Bn = Vector(1.1, 2.2, 3.3)
        
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



def main():
	unittest.main()

if __name__ == "__main__":
	main()
