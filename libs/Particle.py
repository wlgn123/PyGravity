from Vector import Vector
class Particle(object):
    def __init__(self, P, V, m):
        self.P = P        #particles position vector
        self.V = V        #Particles velocity vector
        self.m = m        #particles mass
        
    def move(self):
        new_pos = Vector.add(P, V)
        self.P = new_pos
