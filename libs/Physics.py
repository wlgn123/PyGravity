from decimal import *
from Particle import Particle
from Vector import Vector
import csv
class Physics(object):
    def __init__(self):
        self.objects = []
        self.timestep = 1
        self.total_steps = 0
        self.dimension = 3
        self.set_prec(100)
    
    def set_prec(self, a):
        getcontext().prec = a

    def add_obj(self, obj):
        for item in self.objects:
            if obj.name == item.name:
                raise ValueError("duplicate name found, not adding last entry")
                return
        self.objects.append(obj)


    def Fg(self, A, B):
        G = Decimal('6.67384e-11')
        r =  A.P - B.P   #vector between two particles
        r_squared = r.magnitude() ** 2  # dist between A, B squared
        f_mag = (G*A.m.magnitude()*B.m.magnitude())*(r_squared**(-1))
        f_vec = r.unit() * f_mag
        return f_vec

    def sum_Fg_one_particle(self, A):
        force_list = []
        for particle in self.objects:
            if particle != A:
                force_list.append(self.Fg(particle, A))
        f = lambda a,b: a+b
        total_force = reduce(f, force_list)
        return total_force

    def apply_gravitational_acceleration(self, A):
        total_Fg_A = self.sum_Fg_one_particle(A)
        acceleration = total_Fg_A * (1/A.m.magnitude())
        A.accelerate(acceleration,self.timestep)

    def step_all(self):
        for item in self.objects:
            self.apply_gravitational_acceleration(item)
        for item in self.objects:
            item.move(self.timestep)
        self.total_steps += 1

    def read_file(self, path):
        with open(path, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=':', quotechar='|')
            for row in spamreader:
                try:
                    if self.dimension == 3:
                        self.add_obj(Particle(row[0], Vector(row[1:4]), Vector(row[4:7]), Vector(row[7:]) ) )
                    elif self.dimension == 2:
                        self.add_obj(Particle(row[0], Vector(row[1:3]), Vector(row[3:5]), Vector(row[5:]) ) )
                except ValueError as e:
                    print e



#At delta time to accelerate and move methods in Particle class
