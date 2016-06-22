# PyGravity
## Install


    ./build.sh -i                   # build and install
    ./build.sh -t                   # run unit tests
    
Note: The unit tests run against the installed module, not the source.

## About
Gravity Simulator.

## Documentaion
http://russloewe.github.io/PyGravity
#### core 
The main docs are generated with Sphinx. Generate
them yourself by running 
    
    ./build.sh -d
    
in the project root.

#### example
There are serveral examples that demsonstrate PyGravity in the ./examples folder. So far there is one 
main file called 2D_Physics.py which demonstrates several key features. There are also a collection of 
ipython notebooks. 

Documentation illustrating a couple of examples to be posted.

## Features
- Loading a set of objects from a CSV file.
- Saving to a CSV file.
- Adjusting precision for speed vs precision trade-off.
- Adjusting time interval, also allows trade-off between precison and speed.
- Use vector math and physics calculations as a stand alone tool, outside of the simulator.


