import numpy as np
import matplotlib.pyplot as plt
from PyGravity import Physics, Particle, Vector, round_sig
import PyGravity

base = PyGravity.PyGravity()
base.dimension = 3

base.set_reader_type('CSV')
base.read_file('example_data.csv')

base.Physics.timestep = 60
base.Physics.prec = 100

total_mass = 0
for item in base.Physics.objects:
    total_mass += item.m[0]
am = round_sig(100*base.Physics.objects[0].m[0]/total_mass, 1)
bm = round_sig(100*base.Physics.objects[1].m[0]/total_mass,1)
cm = round_sig(100*base.Physics.objects[2].m[0]/total_mass,1)
dm = round_sig(100*base.Physics.objects[3].m[0]/total_mass,1)
print am, bm, cm
ax = []
ay = []
bx = []
by = []
cx = []
cy = []
dx = []
dy = []
for i in range(10):
    if i % 1 == 0:
        print base.Physics.objects[1].round(2)
    ax.append(base.Physics.objects[0].P[0])
    ay.append(base.Physics.objects[0].P[1])
    bx.append(base.Physics.objects[1].P[0])
    by.append(base.Physics.objects[1].P[1])
    cx.append(base.Physics.objects[2].P[0])
    cy.append(base.Physics.objects[2].P[1])
    dx.append(base.Physics.objects[3].P[0])
    dy.append(base.Physics.objects[3].P[1])

    base.Physics.step_all()
    
print 'Time: ', (base.Physics.total_steps), 'mins'
plt.scatter(ax, ay, s=am, c='b', alpha=0.5)
plt.scatter(bx, by, s=bm, c='r', alpha=0.5)
plt.scatter(cx, cy, s=cm, c='g', alpha=0.5)
plt.scatter(dx, dy, s=dm, c='y', alpha=0.5)
plt.show()
