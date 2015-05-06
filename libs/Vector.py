
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
 

    
