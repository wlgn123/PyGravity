import numpy as np
from numpy import linalg as LA
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
        r = np.subtract(A.P, B.P)  #vector between two particles
        r_hat = np.multiply((1/LA.norm(r)), r)    #unit vector of r
        r_squared = LA.norm(r) ** 2  # dist between A, B squared
        f_mag = (G*ma*mb)/r_squared
        f_vec = np.multiply(f_mag, r_hat)
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
