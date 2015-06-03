from decimal import *
from Particle import Particle
class Physics(object):
    def __init__(self):
        self.objects = []

    def add_obj(self, obj):
        for item in self.objects:
            if obj.name == item.name:
                raise ValueError("duplicate name found, not adding last entry")
                return
        self.objects.append(obj)

    @staticmethod
    def Fg(A, B):
        G = Decimal('6.67384e-11')
        r = A.P -  B.P  #vector between two particles
        r_hat =r    #unit vector of r
        r_squared = r.magnitude() ** 2  # dist between A, B squared
        f_mag = (G*A.m*B.m)*(r_squared**(-1))
        f_vec = r.unit() * f_mag
        return f_vec

    def sum_Fg_one_particle(self, A):
        force_list = []
        for particle in self.objects:
            if particle != A:
                force_list.append(self.Fg(particle, A))
        f = lambda a,b: np.add(a,b)
        total_force = reduce(f, force_list)
        return total_force

    def apply_gravitational_acceleration(self, A):
        total_Fg_A = self.sum_Fg_one_particle(A)
        acceleration = np.multiply((1/A.m), total_Fg_A)
        A.accelerate(acceleration)

#At delta time to accelerate and move methods in Particle class
