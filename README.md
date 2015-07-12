# PyGravity
## Install


    sudo python setup.py install
    python setup.py test            # run unit tests
    
Note: The unit tests run against the installed module, not the source.

## About
#### What is it
A library to simulate the motion due to gravity for any number of objects of any size to a high degree of precision. This program allows you to create any number of particles or asteriods or planets at any location in two or three dimensions and watch how they orbit eachother. 
##### What it is not

-  In one word: fast. Using the awesomness of numpy's speed was scrapped for the accuracy of Decimal. So while you'll die of old age trying to simulate a very large system for more then a few seconds, you will be able to see how fast gravity could pull two baseballs together in deep space without the simulator rounding the extremly weak forces to zero.
-  This is also not realtivistic. So no black holes, no orbits near the speed of light, no time dialation. 

## Documentaion
##### core 
The main docs are generated with Sphinx, find them at http://russloewe.com/PyGravity/index.html or generate
them yourself by running 
    
    make html
    
in ./documentation folder

##### example
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
- move Physics.objects to seperate attribute object. ditto to dimension, precision, timestep, etc.


