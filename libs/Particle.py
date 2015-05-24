import numpy as np
class Particle(object):
    def __init__(self, P, V, m):
        self.P = P        #particles position vector
        self.V = V        #Particles velocity vector
        self.m = m        #particles mass
        
    def move(self):
        new_pos = np.add(self.P, self.V)
        self.P = new_pos
        
    def accelerate(self, A):
        new = np.add(self.V, A)
        self.V = new
        
