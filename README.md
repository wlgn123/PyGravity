# PyGravity
## Install


    ./build.sh -i                   # build and install
    ./build.sh -t                   # run unit tests
    
Note: The unit tests run against the installed module, not the source.

## About
GRavity Simulator.

## Documentaion
#### core 
The main docs are generated with Sphinx, find them at http://russloewe.com/PyGravity/index.html or generate
them yourself by running 
    
    ./build.sh -d
    
in the project root.

#### example
There are serveral examples that demsonstrate PyGravity in the ./examples folder. So for there is one 
main file called 2D_Physics.py which demonstrates several key features. There are also a collection of 
ipython notebooks. 

Documentation illustrating an example usage can be found under ./docs/PyGravity_doc.tex. The 
tex file can be compiled into a PDF with 

    make all clean

Pdflatex is required.

## Features
- Loading a set of objects from a CSV file.
- Saving to a CSV file.
- Adjusting precision for speed vs precision trade-off.
- Adjusting time interval, also allows trade-off between precison and speed.
- Use vector math and physics calculations as a stand alone tool, outside of the simulator.

## TODO
- Gravitational fields. 
- multiprocessor
- ~~Save to CSV~~
- Save to xml
- better docs


