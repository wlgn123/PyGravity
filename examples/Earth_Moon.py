import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

import PyGravity

#PyGravity stuff
base = PyGravity.PyGravity()    # start by making base instance 
base.read_file('earth_moon.xml')

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

one_hour = 60*60
one_day = one_hour* 24

for i in range(one_day * 27 ):
	# Show what day the simulator is on
	if i % one_day == 0:
		print 'Day: ', i/one_day
		
	#plot a point for every hour
	if i % one_hour == 0:
		Ax.append(float(base.particle_list[0].P[0]))
		Ay.append(float(base.particle_list[0].P[1]))
		Az.append(float(base.particle_list[0].P[2]))
		Bx.append(float(base.particle_list[1].P[0]))
		By.append(float(base.particle_list[1].P[1]))
		Bz.append(float(base.particle_list[1].P[2]))

		if PyGravity.Physics.escaping(base.particle_list) != []:
			print 'escaping',PyGravity.Physics.escaping(base.particle_list)
			break


	base.step_all()

print 'Time: ', (base.currant_time)/(60*60), 'hrs'


ax.plot(Ax, Ay, Az, label='Earth')
ax.plot(Bx, By, Bz, label='Moon')
ax.legend()


plt.show()
