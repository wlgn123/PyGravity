from distutils.core import setup, Extension

module1 = Extension('vector_math',
					include_dirs = ['/usr/local/include'],
                    sources = ['vector_math.c'],
                    libraries = ['mpfr'],
                    library_dirs = ['/usr/local/lib']
                    )

setup (name = 'vector_math',
       version = '1.0',
       description = 'This is the C version of Grav_Accel',
       ext_modules = [module1],
       inplace = 1)
