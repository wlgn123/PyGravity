.. PyGravity documentation master file, created by
   sphinx-quickstart on Tue Jun 30 02:30:18 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyGravity's documentation!
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
	./build.sh

The build script is a pretty straight forward bash script. It will enter
the src directory and use Python's setup tool to compile the C source 
code for the extensions and install them into the Python directory.


It will then go back to top level and install the rest of the PyGravity 
module. Afterwards it will invoke the unittests and if those pass it will
run Sphinx's makefile to make the html docs.

It also checks the return values on each of the setup.py calls, and will 
inform you if any step failed. 

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
	
	>>> A = Particle('A', Vector([0]), Vector([0]), Vector([1.0]))
	>>> B = Particle('B', Vector([10]), Vector([0]), Vector([1.0]))
	
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

	>>> A = Particle('A', Vector([0, 0]), Vector([0,0]), Vector([1.0]))
	>>> B = Particle('B', Vector([10,0]), Vector([0,0]), Vector([1.0]))
	>>> C = Particle('C', Vector([10,10]), Vector([0,0]), Vector([1.0]))
	
Now to find the total force acting on a particle we can call Total_Grav_Force.
This function takes a list of particles and iterates through them summing all the 
different froce vectors acting on one particle. So to find the total force 
acting on Particle A::

	>>> print Physics.Total_Grav_Force([A,B,C], A)
	(-9.03339876028e-13,-2.35955876028e-13)

We can also find the acceleration acting on an object with the Grav_Accel,
and accompaining Sum_Grav_Accel method::

	>>> print Physics.Sum_Grav_Accel([A,B,C], A)
	(9.03339876028e-13,2.35955876028e-13)
	
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
