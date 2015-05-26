import sympy
from bigfloat import *
class Vector(object):
    def __init__(self, array):
        self.vector = self.makebig(array)

    def __str__(self):
        string = '('
        c = 0
        for item in self.vector:
            if c!=0:
                string = string + ',' + str(item)
            else:
                string = string  + str(item)
            c += 1
        string = string + ')'

        return string

    def __add__(self, other_vector):
        if self.array_mismatch(other_vector):
            raise ValueError('vector dimension doesnt match')

        new_array = []
        for index, val in enumerate(self.vector):
            new_array.append(val + other_vector.vector[index])
        return Vector(new_array)

    def __radd__(self, other_vector):
        new_vector = []
        for index, val in enumerate(self.vector):
            new_array.append(val + other_vector.vector[index])

        return Vector(new_array)

    def __sub__(self, other_vector):
        new_array = []
        for index, val in enumerate(self.vector):
            new_array.append(val - other_vector.vector[index])
        return Vector(new_array)

    def __rsub__(self, other_vector):
        new_array = []
        for index, val in enumerate(self.vector):
            new_array.append(val - other_vector.vector[index])
        return Vector(new_array)

    def __eq__(self, other_vector):
        i=0
        for element in self.vector:
            try:
                if element != other_vector.vector[i]:
                    return False
            except Exception:
                return False
            i += 1
        return True

    def makebig(self, array):
        new_array = []
        for val in array:
            new_array.append(BigFloat.exact(str(val), precision=200))
        return new_array

    def array_mismatch(self, other):
        if len(self.vector) != len(other.vector) :
            return True
        else:
            return False

    @staticmethod
    def times_scalar(a, A):
        new = Vector(A.x * a,
                     A.y * a,
                     A.z * a)
        return new

    @staticmethod
    def magnitude(A):
        mag = sympy.sqrt(A.x**2 + A.y**2 + A.z**2)
        return mag

    @staticmethod
    def unit(A):
        mag = Vector.magnitude(A)
        new = Vector.times_scalar(1.0/mag, A)
        return new






