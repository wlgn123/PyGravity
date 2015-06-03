from Vector import Vector
class Particle(object):
    def __init__(self, name, P, V, m):
        self.P = P        #particles position vector
        self.V = V        #Particles velocity vector
        self.m = m        #particles mass
        self.name = name

    def move(self, timestep):
        new_pos = self.P + self.V*timestep
        self.P = new_pos

    def accelerate(self, A, timestep):
        new = self.V + A*timestep
        self.V = new

    def __str__(self):
        particle_str = self.name + ': Position: ' + str(self.P) + ', Velocity: ' + str(self.V) + ', Mass: ' + str(self.m)
        return particle_str

    def round(self, n):
         particle_str = self.name + ': Position: ' + str(self.P.round(n)) + ', Velocity: ' + str(self.V.round(n)) + ', Mass: ' + str(self.m.round(n))
         return particle_str

