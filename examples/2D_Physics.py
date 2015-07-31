import numpy as np
import matplotlib.pyplot as plt
import sys
import PyGravity

base = PyGravity.PyGravity()    # start by making base instance 
base.set_dimension(3)           # not needed for dim 3, but here it is


base.read_file('example_data.csv')

base.set_time_interval(5000000000)
base.set_fast(True)

ax = []
ay = []
bx = []
by = []
cx = []
cy = []
dx = []
dy = []
for i in range(20000):
	try:
		if i % 200 == 0:
			print i
			
			ax.append(base.particle_list[0].P[0])
			ay.append(base.particle_list[0].P[1])
			bx.append(base.particle_list[1].P[0])
			by.append(base.particle_list[1].P[1])
			cx.append(base.particle_list[2].P[0])
			cy.append(base.particle_list[2].P[1])
			dx.append(base.particle_list[3].P[0])
			dy.append(base.particle_list[3].P[1])

			if PyGravity.Physics.escaping(base.particle_list) != []:
				print PyGravity.Physics.escaping(base.particle_list)
				break
			
		
		base.step_all_verlet()
		
	except RuntimeWarning:
		sys.exit(1)
	
print 'Time: ', (base.currant_time), 'mins'
plt.scatter(ax, ay, s=10, c='b', alpha=0.5)
plt.scatter(bx, by, s=10, c='r', alpha=0.5)
plt.scatter(cx, cy, s=10, c='g', alpha=0.5)
plt.scatter(dx, dy, s=10, c='y', alpha=0.5)
plt.show()
