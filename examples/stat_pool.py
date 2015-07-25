import numpy as np
import profile
import PyGravity

base = PyGravity.PyGravity()    # start by making base instance
base.set_dimension(3)           # not needed for dim 3, but here it is


base.read_file('bigset.csv')

base.set_time_interval(1000)
base.set_fast(True)

def pol(a):
    for i in range(a):
        print base.particle_list[0].round(2),i
    base.step_all()

def no_pol(a):
    for i in range(a):
        print base.particle_list[0].round(2),i
    base.step_all_verlet()

profile.run('pol(2)')
profile.run('no_pol(2)')

