from Vector import Vector
from Particle import Particle
class Physics(object):
    def __init__(self):
        self.objects = []

    def add_obj(self, obj):
        self.objects.append(obj)

    @staticmethod
    def Fg(A, B):
        G = 6.67384 * 10**(-11)
        ma = A.m
        mb = B.m
        r = Vector.sub(A.P, B.P)  #vector between two particles
        r_hat = Vector.unit(r)    #unit vector of r
        r_squared = Vector.magnitude(r) ** 2  # dist between A, B squared
        f_mag = (G*ma*mb)/r_squared
        f_vec = Vector.times_scalar(f_mag, r_hat)
        return f_vec

    def sum_Fg_one_particle(self, A):
        force_list = []
        for particle in self.objects:
            if particle != A:
                force_list.append(self.Fg(particle, A))
        f = lambda a,b: Vector.add(a,b)
        total_force = reduce(f, force_list)
        return total_force

    def apply_gravitational_acceleration(self, A):
        total_Fg_A = self.sum_Fg_one_particle(A)
        acceleration = Vector.times_scalar((1/A.m), total_Fg_A)
        #print "acceleration: ", acceleration.show
        A.accelerate(acceleration)

#For summing the force of gravity on the particle, calcuate
# the force for each particle, add to list the use fancy python reduce
# or  something to sum the list using the Vector.add() function
