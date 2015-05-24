"""
This shows a test particle A as it falls between two large objects back and forth
"""
import numpy as np
import matplotlib.pyplot as plt
<<<<<<< HEAD
from mpl_toolkits.mplot3d import Axes3D
from libs import  Particle, Physics
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
A = Particle(np.array([0,10.00,0]), np.array([0,0,0]), 1)
B = Particle(np.array([-10,0,0]), np.array([0,0,0]), 100000000080)
C = Particle(np.array([10,0,0]), np.array([0,0,0]), 100000000000)
=======
from libs import Vector, Particle, Physics

A = Particle(Vector(0,10.00,0), Vector(0,0,0), 1)
B = Particle(Vector(-10,0,0), Vector(0,0,0), 10000000000)
C = Particle(Vector(10,0,0), Vector(0,0,0), 10000000000)
>>>>>>> 7b9e2e9d1394a1f65d529aaabffad2c35656f298
base = Physics()

base.add_obj(A)
base.add_obj(B)
base.add_obj(C)
N = 50
x = []
y = []

<<<<<<< HEAD
for i in range(400):
    base.apply_gravitational_acceleration(base.objects[0])
    base.objects[0].move()
    x.append(i)
    y.append(base.objects[0].P[1])
    ax.scatter(base.objects[0].P[0], base.objects[0].P[1], i, c='r', marker='o')
=======
for i in range(1000):
    base.apply_gravitational_acceleration(base.objects[0])
    base.objects[0].move()
    x.append(i)
    y.append(base.objects[0].P.y)
>>>>>>> 7b9e2e9d1394a1f65d529aaabffad2c35656f298

colors = np.random.rand(N)
area = 4

<<<<<<< HEAD
#plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

=======
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()
>>>>>>> 7b9e2e9d1394a1f65d529aaabffad2c35656f298
