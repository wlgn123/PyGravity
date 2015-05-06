
class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.show = "(" + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ')'
       # print "particle created at (", x, ',', y, ',', z, ')'
    
    def add(self, vector):
        new = Vector(self.x + vector.x, 
                     self.y + vector.y,
                     self.z + vector.z)
        
        return new
 
