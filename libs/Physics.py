from Vector import Vector
from Particle import Particle
class Physics(object):
    def __init__(self):
        self.objects = []
        
    def add_obj(self, obj):
        self.objects.append(obj)
    
    @staticmethod
    def Fg(A, B):
        pass 
#For summing the force of gravity on the particle, calcuate
# the force for each particle, add to list the use fancy python reduce
# or  something to sum the list using the Vector.add() function
