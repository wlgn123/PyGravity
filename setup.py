from distutils.core import setup, Extension
from distutils.cmd import Command
from tests import test
import os


setup(name='PyGravity',
	version='1.01',
	description='Gravity Simulator',
	url='http://github.com/russloewe/PyGravity',
	author='Russell Loewe',
	author_email='russloewe@gmail.com',
	license='MIT',
	packages=['PyGravity'],
	zip_safe=False
	)


