from distutils.core import setup
from distutils.cmd import Command
from tests import test


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        test.main()

setup(name='PyGravity',
	version='1.01',
	description='High Precision Gravity Simulator',
	url='http://github.com/russloewe/PyGravity',
	author='Russell Loewe',
	author_email='russloewe@gmail.com',
	license='MIT',
	packages=['PyGravity'],
	zip_safe=False,
	cmdclass={'test': TestCommand}
	)


