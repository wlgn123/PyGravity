import math
class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.show = "(" + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ')'
       # print "particle created at (", x, ',', y, ',', z, ')'
    
    @staticmethod
    def add(A, B ):
        new = Vector(A.x + B.x, 
                     A.y + B.y,
                     A.z + B.z)
        return new
        
    @staticmethod
    def sub(A, B):
        new = Vector(A.x - B.x,
                     A.y - B.y,
                     A.z - B.z)
        return new
        
    @staticmethod
    def times_scalar(a, A):
        new = Vector(A.x * a, 
                     A.y * a,
                     A.z * a)
        return new
        
    @staticmethod
    def magnitude(A):
        mag = math.sqrt(A.x**2 + A.y**2 + A.z**2)
        return mag
        
    @staticmethod
    def unit(A):
        mag = Vector.magnitude(A)
        new = Vector.times_scalar(1.0/mag, A)
        return new
        
    
 
    

    
