# PyGravity

#### What is it
A library to simulate the motion due to gravity for any number of objects of any size to a high degree of precision. This program allows you to create any number of particles or asteriods or planets at any location in two or three dimensions and watch how they orbit eachother. 
##### What it is not

-  In one word: fast. Using the awesomness of numpy's speed was scrapped for the accuracy of Decimal. So while you'll die of old age trying to simulate a very large system for more then a few seconds, you will be able to see how fast gravity could pull two baseballs together in deep space without the simulator rounding the extremly weak forces to zero.
-  This is also not realtivistic. So no black holes, no orbits near the speed of light, no time dialation. 

##### Under The Hood
THe precsion is excetued using Python's built in Decimal module. There is an optoion to specify the global Decimal precision so you can quickly deicide on a compromise between accuruarcy and speed.

#### Features
Loading a set of objects from a CSV file, adjusting precision, adjusting time interval.
#### Examples
I included a couple exmple Ipython notebooks in the repo. The main one is called "2D_Physics.ipynb" or also "2d_Physics.py". These examples really use most of the features in one file to graph a ring of planets.
#### Documentaion
Documentation at TBA.
There is some at ./docs/PyGravity.pdf but it is sorely outdated

#### TODO
- Gravitational fields. 
- Save to CSV
- better docs


