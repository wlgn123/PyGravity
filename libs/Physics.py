from Vector import Vector
from Particle import Particle
class Physics(object):
    def __init__(self):
        self.objects = []
        
    def add_obj(self, obj):
        self.objects.append(obj)
    
    @staticmethod
    def Fg(B, A):
        G = 6.67384 * 10**(-11)
        ma = A.m
        mb = B.m
        r = Vector.sub(A.P, B.P)  #vector between two particles
        r_hat = Vector.unit(r)    #unit vector of r
        r_squared = Vector.magnitude(r) ** 2  # dist between A, B squared
        f_mag = (G*ma*mb)/r_squared
        f_vec = Vector.times_scalar(f_mag, r_hat)
        return f_vec
    
#For summing the force of gravity on the particle, calcuate
# the force for each particle, add to list the use fancy python reduce
# or  something to sum the list using the Vector.add() function
