from math import sqrt
import numpy as np
from pygravity_grav_accel import ext_grav_accel

'''
.. module:: Physics
   :platform: Unix
   :synopsis: Main Physics Function Bundle.

.. moduleauthor:: Russell Loewe <russloewe@gmail.com>
.. todo::
    Create a seperate object to hold particle list, vector deminsion
    and time step and time counter
'''
# global constant
G = 6.67384e-11

def grav_force(a_part, b_part):
    '''
    Calculates the force of gravity between two particles. Uses Newton's
    Law of Gravity. Gravitational constant is in standtard metric units.

    :param: A(Particle): First particle

    :param: B(Particle): Second Particle

    :returns: Force(Vector): Force acting on particle A as a Vector.
    '''
    r_vec = a_part.P-b_part.P   # vector between two particles
    r_norm = np.linalg.norm(r_vec)
    r_squared = r_norm ** 2  # dist between A, B squared
    f_mag = (G*a_part.m * b_part.m)*(r_squared**(-1))
    f_vec = r_vec * (f_mag/r_norm)
    return f_vec


def total_grav_force(particle_list, particle):
    '''
    Finds the the total force of gravity acting on one particle.
    The force of gravity acting on the supplied particle is claculated
    for every particle in the global particle list. The result is then
    summed and returned.

    :para: particle_list(list): List of particle objects

    :param: parrticle(Particle): Particle for which the force of gravity is
        being calculated.

    :returns: Force of gravity as a Vector Object.

    '''
    force_list = []
    for _particle in particle_list:
        if _particle != particle:
            force_list.append(grav_force(_particle, particle))
    force = lambda a, b: a+b
    total_force = reduce(force, force_list)
    return total_force


def grav_accel(a_part, b_part):
    '''
    Calculate the acceleration between particle A and B due to
    gravity. Uses math shortcuts to reduce total number of calculations
    as apposed to using Grav_Force / mass to find acceleration.

    :param: A(Vector): The first vector.
    :param: B(Vector): The second vector.

    :returns: The acceleration as a Vector Object.

    .. note:: Force returned is the force acting on B, the second
        argument.


    .. todo:: Add formated math example, ie learn sphinx embedded math

    .. todo:: double check consistancy of (A,B) accross all physics
        functions

    '''
    r_vec = b_part.P-a_part.P   # vector between two particles
    r_norm = np.linalg.norm(r_vec)

    r_cube = r_norm ** 3  # dist between A, B cubed
    acc = G * b_part.m / r_cube
    return r_vec * acc  # the normilizer, r.unit, is hidden in r_cube


def c_grav_accel(a_part, b_part):
    '''
    Wrapper for the pygravity_grav_accel extension. Does same thing as
    the Grav_Accel function but in pre-compiled C.

    :param: A(Particle) first particle
    :param: B(Particle) second particle
    :returns: Acceleration as a Vector

    This wraps the C extension pygravity_grav_accel.grav_accel . This
    function provided a great speed up when the high precision Vector
    class was the backbone for the vectors. Now we have moved to numpy
    for the vector calculations. Numpy isn't as precise as the Vector
    class, but when the value of the gravitational constant, G, has only
    like 6 significant digits it is deffiniatly worth it to scrap really
    high precision. This, along with the vector class remains incase it is
    needed later. But, for the moment, it is just an example of using
    C to extend Python.

    The call signature for grav_accel() is as follows:

    .. code-block:: python

        grav_accel(
            precision(int),
            mass(string),
            A.x(string),
            A.y(string),
            A.z(string),
            B.x(string),
            B.y(string),
            B.z(string)
            )


    '''
    acc_string = ext_grav_accel(
        b_part.m,
        a_part.P[0],
        a_part.P[1],
        a_part.P[2],
        b_part.P[0],
        b_part.P[1],
        b_part.P[2]
        )
    acc_vec = np.array(list(acc_string), dtype=float)
    return acc_vec


def proto_acc(a_part, b_part):
    '''
    Calculate the acceleration between two objects,
    leaving the mass part out. Therefore:

    .. code-block:: python

        A = Obj1
        B = Obj2
        proto = Proto_Acc(A, B)
        A_Acc = proto * B.mass         #Acceleration on A
        B_Acc = proto * (-1.0)*A.mass   # Acceleration on B

    Seperating the calculations into two steps like this will allow
    for optinmizing acceleration calculations for a large set of
    objects.
    '''
    r_vec = b_part.P-a_part.P
    r_mag = np.linalg.norm(r_vec)   # r_mag = ||A-B||
    r_mag_cubed = r_mag * r_mag * r_mag

    return r_vec * (G/r_mag_cubed)


def sum_grav_accel(particle_list, a_part, fast_flag=False):
    '''
    Sum the total acceleration acting on a particle by using the
    Grav_Accel function and iterating through the particle list.

    :param: global_container(Global_Container): List of particles
        to iteratethrough.

    :param: A(Vector): Vector to calculate acceleration for.
    :returns: Acceleraton as a Vector Object
    .. todo:: need unittest.
    '''
    if fast_flag:
        acc_list = []
        for particle in particle_list:
            if particle != a_part:
                acc_list.append(c_grav_accel(a_part, particle))
        total_acc = reduce(lambda a, b: a+b, acc_list)
        return total_acc
    else:
        acc_list = []
        for particle in particle_list:
            if particle != a_part:
                acc_list.append(grav_accel(a_part, particle))
        total_acc = reduce(lambda a, b: a+b, acc_list)
        return total_acc


def escape_velocity(a_part, b_part):
    '''
    Calculate the escape velocity between two objects.

    :param: A(Particle): First particle.

    :param: B(Particle): Second particle.

    :returns: Escape velocity as a Vector Object.
    '''
    r_vec = np.linalg.norm(a_part.P-b_part.P)  # distance between A and B
    esc = sqrt((G*b_part.m)/r_vec)        # formula for escape velocity
    return esc


def total_escape_velocity(particle_list, a_part):
    '''
    Find the total escape velocity acting on a particle with repect
    to the rest of the active particles in the simulation.

    :param: global_containter(Global_Container): Attribute container.

    :param: A(Vector): Particle to find escape velocity for.

    '''
    esc_list = []
    for item in particle_list:
        if a_part != item:
            esc_list.append(escape_velocity(a_part, item))
    return reduce(lambda a, b: a+b, esc_list)


def escaping(particle_list):
    '''
    Find all the particles in the currant system that are exceeding
    the escape velocity for said system of particles

    :param: global_container(Global_Container): Container object for
        particles.

    :returns: List of particles exceeding escape velocity.
    '''
    escap_list = []
    for item in particle_list:
        total_esc = total_escape_velocity(particle_list, item)
        if total_esc < np.linalg.norm(item.V):
            escap_list.append(item.name)
    return escap_list


def _step_verlet_one(pair, delta_t):
    '''
    First pass for the verlet method utilizing the proto_accel and
    half_list method

    ::param:: Tple of Particle objects
    '''
    a_part, b_part = pair
    proto = proto_acc(a_part, b_part)
    a_acc = proto * b_part.m
    b_acc = proto * (-1.0) * a_part.m
    a_part.store_acc(a_acc)
    b_part.store_acc(b_acc)
    a_part.P = a_part.P + a_part.V + a_acc*(delta_t/2.0)
    b_part.P = b_part.P + b_part.V + b_acc*(delta_t/2.0)


def _step_verlet_two(pair, delta_t):
    '''
    Second pass for the verlet method utilizing the proto_accel and
    half_list method
    ::param:: Tple of Particle objects
    '''
    a_part, b_part = pair
    proto = proto_acc(a_part, b_part)
    a_acc = proto * b_part.m
    b_acc = proto * (-1.0) * a_part.m
    a_part.V = (a_part.A + a_acc)*(delta_t/2.0)
    b_part.V = (b_part.A + b_acc)*(delta_t/2.0)


def _step_euler(part_list, flag, delta_t, part):
    '''
    helper for step_all function
    '''
    acc = sum_grav_accel(part_list, part, flag)
    part.accelerate(acc, delta_t)
    part.move(delta_t)
