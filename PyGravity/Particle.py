'''
.. module:: Particle
   :platform: Unix
   :synopsis: Particles.

.. moduleauthor:: Russell Loewe <russloewe@gmail.com>

'''
import numpy as np


class Particle(object):
    '''
    Class for creating a Particle object. Depends on Vectors.
    '''
    def __init__(self, name, pos, vol, mass):
        '''
        Creates particle with initial values

        :param: name(string): Name of the particle. Used for keeping
            track of particles when reading or writing to data files, or
            printing to console.
        :param: P(Vector): Postitional vector of particle.
        :param: V(Vector): Velocity vector of particle.
        :param: m(Vector): Mass of the Particle. Represented as a 1
            dimensional vector.

        .. note:: Mass is represented as a 1D vector. A 1D vector is the
            same as a scalar, but by using vector objects the abstraction
            makes the code in the Physics Module a little bit more straight
            forward. It is possible to use a 2D or higher vector for mass
            but unless new physics is discovered this won't make sense.

        .. note:: The unites are not specified. It is up to the calling
            function to keep track of units.
        '''
        # check inputs
        assert type(pos) is np.ndarray or list, \
            'Only numpy arrays, or lists are supported for Position Vector'
        assert type(vol) is np.ndarray or list, \
            'Only numpy arrays, or lists are supported for Velocity Vector'

        if mass is not float:
            try:
                mass = float(mass)
            except:
                raise TypeError("Particle mass couldn't be converted to float")

        self.pos = np.array(pos, dtype=float)    # particles position vector
        self.vol = np.array(vol, dtype=float)    # Particles velocity vector
        self.mass = mass                           # particles mass
        self.name = name

    def move(self, delta_t):
        '''
        Moves the particle based on the current velocity stored in
        self.V by the specified time_step. Example

        .. code-block:: python

            >>> A_pos = Vector(['1', '1'])
            >>> A_veloc = Vector(['1', '2'])
            >>> A_mass = Vector(['1'])
            >>> A = Particle('A', A_pos, A_veloc, A_mass)
            >>> print A
            A: Position: (1,1), Velocity: (1,2), Mass: (1)
            >>> A.move(1)
            >>> print A
            A: Position: (2,3), Velocity: (1,2), Mass: (1)
            >>> A.move(2)
            >>> print A
            A: Position: (4,7), Velocity: (1,2), Mass: (1)

        :param: timestep(int): Increment of time to move by.
        '''
        delta_p = self.vol * delta_t
        new_pos = self.pos + delta_p
        self.pos = new_pos

    def store_acc(self, acc):
        '''
        Store the acceleration vector on the object to
        be retrived later for multipass numeric integrations.
        '''
        assert type(acc) is np.ndarray or list, \
            "Only numpy arrays/lists are supported for Acc Vectors"
        self.acc = np.array(acc, dtype=float)

    def accelerate(self, acc_vec, delta_t):
        '''
        Increase velocity by specified acceleration and timestep.
        Example using same particle from move() function:

        .. code-block:: python

            >>> print A
            A: Position: (1,1), Velocity: (1,2), Mass: (1)
            >>> A_acc = Vector(['1', '1'])
            >>> A.accelerate(A_acc, 1)
            >>> print A
            A: Position: (1,1), Velocity: (2,3), Mass: (1)
            >>> A.accelerate(A_acc, 2)
            A: Position: (1,1), Velocity: (4,5), Mass: (1)

        .. note:: The intention is that the timestep argument is defined
            globaly by the connecting module, and thus timestep for
            accelerate() and timestep for move() should be the same.

        :param: A(Vector): Acceleration vector
        :param: timestep(int): Time increment.
        '''
        assert type(acc_vec) is np.ndarray, \
            "Only numpy arrays/lists are supported for Acc Vectors"
        tot_acc = acc_vec * delta_t
        new_vec = self.vol + tot_acc
        self.vol = new_vec

    def __str__(self):
        particle_str = \
            "{}: Position: {}, Velocity: {}, Mass: {}".format(
                self.name, self.pos, self.vol, self.mass)
        return particle_str
