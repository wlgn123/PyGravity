from distutils.core import setup, Extension

module1 = Extension('pygravity_grav_accel',
					include_dirs = ['/usr/local/include'],
                    sources = ['pygravity_grav_accel.c'],
                    library_dirs = ['/usr/local/lib']
                    )

setup (name = 'pygravity_grav_accel',
       version = '1.0',
       description = 'pre-compiled library for speeding up PyGravity.Physics.Grav_Accel',
       ext_modules = [module1])
