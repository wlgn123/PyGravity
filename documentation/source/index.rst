.. PyGravity documentation master file, created by
   sphinx-quickstart on Tue Jun 30 02:30:18 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyGravity's documentation!
=====================================

Contents:

.. toctree::
   :maxdepth: 2

full source http://github.com/russloewe/PyGravity

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

PyGravity 
=========================
The PyGravity module is the top layer that wraps the project. 
Contains global values for maintaining the state of the system.

.. automodule:: PyGravity.PyGravity
    :members:



Physics
=========================

Performs physics related computations. All calculations that involve 
anythng that is purly physics is contained here. For example, force 
calculations, acceleration caculations. Straight vector math is included 
in the vector module. So this module does not deal with vector lengths,
unit vectors or anything else like that.

      
.. automodule:: PyGravity.Physics
	:members: 


Vectors
========================
He is vector math. Adding, scalar multiplication, vector length, norming 
vectors, and comparing vector dimension or values. All abstracted for 
vectors of any length.

.. automodule:: PyGravity.Vector
    :members:
    
Particles
========================
Particle objects. Depends heavily on vector. 

.. automodule:: PyGravity.Particle
    :members:
    
Data Input Ouptut
========================
This module handles reading and writing the simulation state to disk.
Here we can load or save the current list of particles. 

.. todo:: Complete state saving using xml so computations can be easily
	continued by without prior knowledge of the system parameters.

.. automodule:: PyGravity.Data_IO
    :members:


ToDo
========================


.. todolist::
