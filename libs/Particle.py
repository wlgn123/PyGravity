from Vector import Vector
class Particle(object):
    def __init__(self, P, V, m):
        self.P = P        #particles position vector
        self.V = V        #Particles velocity vector
        self.m = m        #particles mass

    def move(self, timestep):
        new_pos = self.P + self.V*timestep
        self.P = new_pos

    def accelerate(self, A, timestep):
        new = self.V + A*timestep
        self.V = new

    def __str__(self):
        particle_str = 'Position: ' + str(self.P) + '\nVelocity: ' + str(self.V) + '\nMass: ' + str(self.m)
        return particle_str

