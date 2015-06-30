import numpy as np
import matplotlib.pyplot as plt

import PyGravity

base = PyGravity.PyGravity()
base.dimension = 3


base.read_file('example_data.csv')

base.Physics.timestep = 60
base.Physics.prec = 100

ax = []
ay = []
bx = []
by = []
cx = []
cy = []
dx = []
dy = []
for i in range(90):
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
plt.scatter(ax, ay, s=10, c='b', alpha=0.5)
plt.scatter(bx, by, s=10, c='r', alpha=0.5)
plt.scatter(cx, cy, s=10, c='g', alpha=0.5)
plt.scatter(dx, dy, s=10, c='y', alpha=0.5)
plt.show()
