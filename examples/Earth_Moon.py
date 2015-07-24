import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

import PyGravity

#PyGravity stuff
base = PyGravity.PyGravity()    # start by making base instance 
base.set_dimension(3)           # not needed for dim 3, but here it is
#base.read_file('earth_moon.csv')
base.read_file('earth_moon.csv')

base.set_time_interval(1)
base.set_fast(True)

#Plotting stuff

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
Ax = []
Ay = []
Az = []
Bx = []
By = []
Bz = []

one_day = 60*60*24
print PyGravity.Physics.Grav_Accel(base.particle_list[0],base.particle_list[1] ).round(4)
for i in range(one_day * 90 ):
	if i % one_day == 0:
		#print base.particle_list[0].round(10),i
		print base.particle_list[1].P.round(2),i/one_day
	Ax.append(float(base.particle_list[0].P[0]))
	Ay.append(float(base.particle_list[0].P[1]))
	Az.append(float(base.particle_list[0].P[2]))
	Bx.append(float(base.particle_list[1].P[0]))
	By.append(float(base.particle_list[1].P[1]))
	Bz.append(float(base.particle_list[1].P[2]))

	

	if i % 500 == 0:
		if PyGravity.Physics.escaping(base.particle_list) != []:
			print 'escaping',PyGravity.Physics.escaping(base.particle_list)
			break


	base.step_all_verlet()
	#base.step_all()

print 'Time: ', (base.currant_time)/(60*60), 'hrs'

#ax.set_xlim(0, 2.5e1)
#ax.set_ylim(-2.0e1, 2.0e1)
#ax.set_zlim(-2.0e1, 2.0e1)

ax.plot(Ax, Ay, Az, label='Obj A')
ax.plot(Bx, By, Bz, label='Obj B')
ax.legend()
#plt.ylim(-2.0e5, 2.0e5)
#plt.xlim(-2.0e5, 2.0e5)

plt.show()
