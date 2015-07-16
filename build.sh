 #!/bin/bash

cd ./src
if ! python setup.py build ; then
	 echo "VECTOR_MATH SOURCE BUILD FAILED" 
 	 exit 1
fi


if ! sudo python setup.py install --force ; then
	 echo "VECTOR_MATH INSTALL FAILED" 
 	 exit 1
fi
 cd ..

if ! sudo python setup.py install --force ;then
	 echo "PYGRAVITY INSTALL FAILED" 
 	 exit 1
fi

if ! python setup.py test ; then
	 echo "Unititest Faild!" 
 	 exit 1
fi

cd ./documentation
if  make html ; then
 	  cd ..
else
 	 echo "SPHINX BUILD FAILD" 
 	 exit 1
fi
