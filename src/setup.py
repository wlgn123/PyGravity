from distutils.core import setup, Extension

module1 = Extension('vector_math',
					include_dirs = ['/usr/local/include'],
                    sources = ['vector_math.c'],
                    libraries = ['mpfr'],
                    library_dirs = ['/usr/local/lib']
                    )

setup (name = 'PackageName',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [module1])
