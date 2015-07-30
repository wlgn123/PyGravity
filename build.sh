#!/bin/bash


usage () {
	echo "BUILD OPTIONS"
	echo
	echo "-s build and install source files"
	echo "-i install PyGravity module, after building and installing source"
	echo "-t test PyGravity"
	echo "-d Build sphinx docs"
	echo "-c clean source build"
	echo "-a run all"
	echo "-h this "
	echo
	exit 1
}

build_src (){
	cd ./src
	echo "BUILDING SOURCE..."
	echo
	if ! python setup.py build ; then
		 echo "VECTOR_MATH SOURCE BUILD FAILED" 
		 exit 1
	fi
	echo "... DONE"
	echo
	cd ..
}

install_src () {
	echo "INSTALLING SOURCE ..."
	echo
	cd ./src
	if ! sudo python setup.py install --force ; then
		 echo "VECTOR_MATH INSTALL FAILED" 
		 exit 1
	fi
	echo "... DONE"
	echo
	 cd ..
}

install_mod () {
	echo "INSTALLING PYGRAVITY ..."
	echo
	if ! sudo python setup.py install --force ;then
		 echo "PYGRAVITY INSTALL FAILED" 
		 exit 1
	fi
	echo "... DONE"
	echo
}

test_mod () {
	if ! python setup.py test ; then
		 echo "Unititest Faild!" 
		 exit 1
	fi
}

build_docs () {
	echo "BUILDING DOCS ..."
	echo
	cd ./documentation
	if  make html ; then
		  cd ..
	else
		 echo "SPHINX BUILD FAILD" 
		 exit 1
	fi
	echo "... DONE"
	echo
	cd ..
}

clean_build () {
	echo "CLEANING ..."	
	echo
	rm -r ./src/build
	#rm -r ./git/documentation/build
	echo "... DONE"
	echo
}

[[ ! $1 ]] && { usage; }

while getopts hsitda opts; do
   case ${opts} in
      h) usage ;;
      
      s) build_src 
         install_src;;
         
      i) build_src
         install_src
         install_mod ;;
         
      t) test_mod ;;
      
      d) build_docs ;;
      
      a) build_src
         install_src
         install_mod
         test_mod
         build_docs ;;
         
      c) clean_build ;;
      
      ?) usage
         exit ;;
   esac
done

