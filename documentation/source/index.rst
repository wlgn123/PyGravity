.. PyGravity documentation master file, created by
   sphinx-quickstart on Tue Jun 30 02:30:18 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PyGravity  Documentation
=====================================

Class and method docs:

.. toctree::
   :maxdepth: 2
   
   Class_Definitions

full source http://github.com/russloewe/PyGravity

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Installation
====================================
Start by downloading the PyGravity source::

	git clone http::/github.com/russloewe/PyGravity

Then enter the PyGravity directory and run the build script::

	cd PyGravity
	./build.sh -i -t


the -i option will build and install the PyGravity module and the 
-t option will run unittests. For my info on the build commands 
type::

	./build.sh -h

The build script also checks returns values and will fail and print an error 
if on of the build steps or tests fails.

.. note:: The unittests will run after the install against the installed PyGRavity
	module and not the local source. Therefore if the unittests pass you should be 
	good to go. However if you change the source you'll need to reinstall for 
	the unittests to check your work.

Using the Physics Library
============================
PyGravity's particle submodule can be used directly along with the physics functions
without the need to invoke the simulator. For instance if we want to know the force of 
gravity between two particles that are each a kilogram in weight and are positioned 10 
meters apart, we can first use the Particle module to created two particle objects::

	>>> from PyGravity import Particle, Vector
	
	>>> A = Particle('A', [0], [0], 1.0)
	>>> B = Particle('B', [10], [0], 1.0)
	
Then we can use the Physics module to calclate the force of gravity between the 
two objects::

	>>> from PyGravity import Physics
	
	>>> print Physics.Grav_Force(A,B)
	(6.67384e-13)
	
The answer is a 1D vector and the units are in Newtons. A 1D setup is 
appropiate here because we were only looking for the force between two 
objects, which reside on a line. 

For a 2D scenarior we can create three particles which will form a triangle 
on  plane::

	>>> A = Particle('A', [0, 0), [0,0], 1.0)
	>>> B = Particle('B', [10,0], [0,0], 1.0)
	>>> C = Particle('C', [10,10], [0,0], 1.0)
	
Now to find the total force acting on a particle we can call Total_Grav_Force.
This function takes a list of particles and iterates through them summing all the 
different froce vectors acting on one particle. So to find the total force 
acting on Particle A::

	>>> print Physics.Total_Grav_Force([A,B,C], A)
	[-9.03339876028e-13,-2.35955876028e-13]

We can also find the acceleration acting on an object with the Grav_Accel,
and accompaining Sum_Grav_Accel method::

	>>> print Physics.Sum_Grav_Accel([A,B,C], A)
	[9.03339876028e-13,2.35955876028e-13]
	
This is the acceleration vector acting on A. The Grav_Accel function works 
just like the Grav_Force function but takes a math shortcut to find the 
acceleration instead of having to find the force then divide by the mass.

Simple Example
========================

To start using :python:func:'PyGravity', we begin be importing the module and declaring a base 
instance::

	import PyGravity as pg
	
	base = pg.PyGravity()
	
Now taking an example data file from the example directory in the source::

	base.read_file('example_data.csv')
	
From there we can run one of the built in simulators. Either the Euler method::

	base.step_all()

or the Verlet Velocity method::

	step_all_verlet()
	
In small time steps the Verlet Method doesn't offer much of an advantage. However, 
with larger time steps the Verlet Method will conserver energy while the Euler 
Method has a tendancy to send particles flying off in escape velocities in 
situations that clearly violate conservation of energy.

To continue our simulation we can load the data files, set the time_interval and 
run through the simulator loop. For example lets run through the simulation at a 
step of one hour for a week, printing the position of every particle once a day::

	from PyGavity import *
	
	base = PyGravity()
	base.read_file('some_data.xml')
	base.set_time_interval(60*60) # an hour step
	
	for i in range(24*7):
		#only print positions every day
		if i % 24 == 0:
			for item in base.particle_list:
				print item.name, item.P
		
		base.step_all()

To double check if any particles are zipping out of the simulation just check run the escaping() function
from the Physics submodule once every iteration, or every day::

	for i in range(24*7):
		#only print positions every day
		if i % 24 == 0:
			for item in base.particle_list:
				print item.name, item.P
			
			#exit if a particle is escaping from the system and list it
			if Physics.escaping(base.particle_list) != []:
				print Physics.escaping(base.particle_list)
				break
		
		base.step_all()
		
		# here also works for escape checks, but might cause unneeded lag

Simple Example with Graphing
=============================
We can easly take our above 2D example and graph the results with Matplotlib.
Just add the particles' positions on each step or sub-step::

	import matplotlib.pyplot as plt
	import PyGravity

	base = PyGravity.PyGravity()    # start by making base instance 
	base.read_file('example_data.csv')
	base.set_time_interval(100)

	ax = []
	ay = []
	bx = []
	by = []
	cx = []
	cy = []
	dx = []
	dy = []
	
	for i in range(200000):
		if i % 200 == 0:
			#some print statements to watch while the simulator runs
			print i
			print base.particle_list[0].P  
			
			#plot all the postions      
			ax.append(base.particle_list[0].P[0])
			ay.append(base.particle_list[0].P[1])
			bx.append(base.particle_list[1].P[0])
			by.append(base.particle_list[1].P[1])
			cx.append(base.particle_list[2].P[0])
			cy.append(base.particle_list[2].P[1])
			dx.append(base.particle_list[3].P[0])
			dy.append(base.particle_list[3].P[1])
			
			#Stop when a particle starts escaping the system
			if PyGravity.Physics.escaping(base.particle_list) != []:
				print PyGravity.Physics.escaping(base.particle_list)
				break
			
		base.step_all()
		
	print 'Time: ', (base.currant_time), 'mins'
	plt.scatter(ax, ay, s=10, c='b', alpha=0.5)
	plt.scatter(bx, by, s=10, c='r', alpha=0.5)
	plt.scatter(cx, cy, s=10, c='g', alpha=0.5)
	plt.scatter(dx, dy, s=10, c='y', alpha=0.5)
	plt.show()

Generates the image

	.. image:: simple_2d.png
		:scale: 70 %
		

 
 Be careful with the time_interval setting. Too big of a step will
 make it appear that the particles are escaping when in  reality they 
 are just suffering from Euler's Method. The Verlet Method should 
 fix this.



3D Example
========================
 Soon to come!


