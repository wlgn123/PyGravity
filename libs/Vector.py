import sympy
class Vector(object):
    def __init__(self, array):
        self.vector = sympy.Matrix(array)

    def __str__(self):
        return str(self.vector)

    def __add__(self, other_vector):
        new_vector = Vector(self.vector + other_vector.vector)
        return new_vector

    def __radd__(self, other_vector):
        new_vector = Vector(self.vector + other_vector.vector)
        return new_vector

    def __sub__(self, other_vector):
        new_vector = Vector(self.vector - other_vector.vector)
        return new_vector

    def __rsub__(self, other_vector):
        new_vector = Vector(self.vector - other_vector.vector)
        return new_vector
        
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






