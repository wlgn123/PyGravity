from decimal import *
from Particle import Particle
from Vector import Vector

class Physics(object):
    def __init__(self):
        self.objects = []
        self.timestep = 1
        self.total_steps = 0
        self.dimension = 3
        self.set_prec(100)
        self.fast = True

    def set_prec(self, a):
        getcontext().prec = a



    #classic vector form force of gravity
    def Fg(self, A, B):
        G = Decimal('6.67384e-11')
        r =  A.P - B.P   #vector between two particles
        r_squared = r.magnitude() ** 2  # dist between A, B squared
        f_mag = (G*A.m.magnitude()*B.m.magnitude())*(r_squared**(-1))
        f_vec = r.unit() * f_mag
        return f_vec

    # adding all forces together
    def sum_Fg_one_particle(self, A):
        force_list = []
        for particle in self.objects:
            if particle != A:
                force_list.append(self.Fg(particle, A))
        f = lambda a,b: a+b
        total_force = reduce(f, force_list)
        return total_force

    #find acceleration from total force, apply using Particle.accelerate()
    def apply_gravitational_acceleration(self, A):
        total_Fg_A = self.sum_Fg_one_particle(A)
        acceleration = total_Fg_A * (1/A.m.magnitude())
        A.accelerate(acceleration,self.timestep)

    # more direct way to find acceleration, skipping some steps
    def calculate_acc(self,A, B):
        G = Decimal('6.67384e-11')
        r =  A.P - B.P   #vector between two particles
        r_cube = r.magnitude() ** 3  # dist between A, B cubed
        acc = G * B.m[0] / r_cube
        return r * acc

    #adding all acceleration vectors and using Particle.accelerate()
    def fast_accelerate(self, A):
        acc_list = []
        for particle in self.objects:
            if particle != A:
                acc_list.append(self.calculate_acc(particle, A))
        total_acc = reduce(lambda a,b:a+b, acc_list)
        A.accelerate(total_acc, self.timestep)

    #find escape velocity between 2 objects
    def escape_v(self, A, B):
        G = Decimal('6.67384e-11')
        r = (A.P-B.P).magnitude() #distance between A and B
        esc = ((G*B.m[0])/r).sqrt()
        return esc

    def total_escape_v(self, A):
        esc_list = []
        for item in self.objects:
            if A != item:
                esc_list.append(self.escape_v(A, item))
        return reduce(lambda a,b: a+b, esc_list)

    def escaping(self):
        escaping = []
        for item in self.objects:
            total_esc = self.total_escape_v(item)
            if total_esc <= item.V.magnitude():
                escaping.append(item.name)
        return escaping


    def step_all(self):
        for item in self.objects:
            if self.fast == True:
                self.fast_accelerate(item)
            else:
                self.apply_gravitational_acceleration(item)
        for item in self.objects:
            item.move(self.timestep)
        self.total_steps += 1



#At delta time to accelerate and move methods in Particle class
