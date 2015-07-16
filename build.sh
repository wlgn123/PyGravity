 #!/bin/bash
 cd src
 if python setup.py build; then
	cd ..
	mv ./src/build/lib.linux-x86_64-2.7/vector_math.so ./PyGravity/
	rm -r ./src/build
else
	 echo "SRC BUILD FAILED!" 
 	 exit 1
fi

 sudo python setup.py install --force
 if python setup.py test ; then
 	  cd ./documentation
 	  make html
 	  cd ..
 else
 	 echo "Unititest Faild!" 
 	 exit 1
fi


