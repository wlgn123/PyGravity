"""
This shows a test particle A as it falls between two large objects back and forth
"""
import numpy as np
import matplotlib.pyplot as plt
from libs import Vector, Particle, Physics

A = Particle(Vector(0,10.00,0), Vector(0,0,0), 1)
B = Particle(Vector(-10,0,0), Vector(0,0,0), 10000000000)
C = Particle(Vector(10,0,0), Vector(0,0,0), 10000000000)
base = Physics()

base.add_obj(A)
base.add_obj(B)
base.add_obj(C)
N = 50
x = []
y = []

for i in range(1000):
    base.apply_gravitational_acceleration(base.objects[0])
    base.objects[0].move()
    x.append(i)
    y.append(base.objects[0].P.y)

colors = np.random.rand(N)
area = 4

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()
