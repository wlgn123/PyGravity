import unittest
from PyGravity import PyGravity, round_sig, Particle, Physics, Data_IO
from math import sqrt
import numpy as np
import sys
'''
Unit Tests for PyGravity. These Unit tests will run tests against the 
installed PyGravity module and not against the source files in this 
package. So if you modify source, you need to re-install with 
.. code-block:: python

    python setup.py install --force
    
'''

class Round_test(unittest.TestCase):
    def setUp(self):
        pass

    def test_rounding_domain(self):
        a = 0
        self.failUnless(round_sig(a, 1) == 0)

    def test_neg_numbers(self):
        a = -1.20
        self.failUnless(round_sig(a,2) == -1.2)



class Particle_Class_Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_particle_creation(self):
        a = Particle('a',np.array([1,2,3]),
                         np.array([1,1,1]), 
                         55.5)
        self.failUnless(hasattr(a, 'P'))
        self.failUnless(hasattr(a, 'V'))
        self.failUnless(hasattr(a, 'm'))
        self.failUnless(a.name == 'a')

    def test_particle_motion(self):
        a = Particle('a', np.array(['1','2','3']),
                          np.array(['1','1','1']), 
                          55.5)
        a.move(1)
        V = np.array([1,1,1])
        P = np.array([2,3,4])
        self.failUnless(np.array_equal(P, a.P))

    def test_particle_motion2(self):
        a = Particle('a',[1.1,2.1,3.0],
                         np.array([1.1,2.1,3.0]),
                         55.5)
        Accel = np.array([2,2,-4])
        Ans = np.array([3.1, 4.1, -1.0])
        a.accelerate(Accel,1)
        self.failUnless(np.array_equal(Ans, a.V))

    def test_particle_acceleration(self):
        a = Particle('a',np.array([1, 1, 1]), 
                         np.array([1,1,1]), 
                         44)
        Acc = np.array([3, 3, -1])
        V_ans = np.array([4, 4, 0])
        P_ans = np.array([5, 5, 1])
        a.accelerate(Acc,1)
        self.failUnless(np.array_equal(V_ans, a.V))
        a.move(1)
        self.failUnless(np.array_equal(P_ans, a.P))

class Physics_Class_Tests(unittest.TestCase):
    def setUp(self):
        self.part1 = Particle('a',np.array([1,1,1]),
                                  np.array([1,1,1]), 
                                  5)
        self.part2 = Particle('b',np.array([2.0e42,1.0e42,3.0e42]), 
                                  np.array([2.3, 1.2, 4.2]), 
                                  5.0e6)
        part1 = Particle('aa',np.array(['1.00009','1.000009','1.000009']), 
                              np.array(['1.09','1.09','1.09']), 
                              5)
        part2 = Particle('b',np.array([2,2,2]), 
                             np.array([2.3, 1.2, 4.2]), 
                             np.array([10]))
        part3 = Particle('c',np.array(['1.2e20','1.2e21','1.4e10']), 
                             np.array(['1','1','1']), 
                             5)
        part4 = Particle('d',np.array(['1.01e-40','1.3e-40','1.4e-40']), 
                             np.array(['1','1','1']), 
                             5.8e-100)
        part5 = Particle('e',np.array(['1.01e10','1.44440000001110',
                                     '1.00000000000001']), 
                             np.array(['1','1','1']), 
                             5.2)
        part6 = Particle('f',np.array(['1.5','-1.2','-1.5']), 
                             np.array(['1','1','1']), 
                             5.3e48)
        self.part_list = [part1, part2, part3, part4, part5, part6]



    def test_Grav_Force_against_known_answer(self):
        part1 = Particle('a',[1, 1,1 ], 
                             [1, 1, 1], 
                             5.0)
        part2 = Particle('b',[2, 2, 2], 
                             [2.3, 1.2, 4.2], 
                             10)
        answer = np.array([6.42e-10, 6.42e-10,6.42e-10 ])
        force_vec = Physics.Grav_Force(part1, part2)
        self.failUnless(np.allclose(answer, force_vec, 1.0e-6))
        
    def test_force_of_gravity_magnitude_against_known_answer(self):
        part1 = Particle('a',np.array(['1.0','1.0','1.0']), 
                             np.array(['0','0','0']), 
                             5.0e10)
        part2 = Particle('b',np.array(['11.0','1.0','1.0']), 
                             np.array(['0','0','0']), 5.0e10)
        force_vec = Physics.Grav_Force(part1, part2)
        self.failUnless(np.linalg.norm(force_vec) == 1668460000)

    def test_grav_accel_against_known_answer(self):
        A = Particle('a',np.array(['1','1','1']), 
                         np.array([1,1,1]), 5)
        B = Particle('b',np.array(['2','2','2']), 
                         np.array([1,1,1]), 10)
        #the known_answer was calculated by hand and verified w/ wolfram|alpha
        known_answer = np.array([1.28438e-10,
                               1.28438e-10, 1.28438e-10])
        self.failUnless(np.allclose(known_answer , 
                        Physics.Grav_Accel(A,B),
                        1.0e-6))
        
        part6 = Particle('f',np.array(['1.5','-1.2','-1.5']), 
                             np.array(['1','1','1']), 5.3e20)
        known_answer_part_6 = np.array([4.63129113e+08,
                                       -2.03776810e+09,
                                       -2.31564557e+09])
        self.failUnless(np.allclose(known_answer_part_6,
                                    Physics.Grav_Accel(A,part6),
                                    1.0e-6))
        
    def test_Grav_Accel_against_known_answer(self):
        part1 = Particle('a',np.array(['1.0','1.0','1.0']), 
                             np.array([1,1,1]), 5.0)
        
        Acceleration_answer = np.array([6.42e-10, 
                                      6.42e-10,
                                      6.42e-10 ]) * (1/part1.m)
        Acc_vecc_one = (Physics.Grav_Force(part1, self.part_list[1]) * (1/part1.m))
        Acc_vecc_two = Physics.Grav_Accel(part1, self.part_list[1])
        self.failUnless(np.allclose(Acc_vecc_one, Acceleration_answer,
                                    1.0e-6))
        self.failUnless(np.allclose(Acc_vecc_two, Acceleration_answer,
                                    1.0e-6))
        
    def test_Grav_Accl_vs_Grav_Force(self):
        part1 = Particle('a',np.array(['1.0','1.0','1.0']), 
                             np.array([1,1,1]), 5.0)
                             
        for i in self.part_list:
            self.failUnless(
            np.allclose(
                Physics.Grav_Force(part1, i) * (-1.0/part1.m), 
                Physics.Grav_Accel(part1, i),
                1.0e-6)
            )
        
    def test_grav_accel_extension_against_known_answer(self):
        A = Particle('a',[1.0, 1.0, 1.0], [1,1,1], 5.0)
        B = Particle('b',[2.0, 2.0, 2.0], [1,1,1], 10.0)
        #the known_answer was calculated by hand and verified w/ wolfram|alpha
        known_answer = np.array([1.28438e-10, 1.28438e-10, 1.28438e-10])
        Acc_vec_one = Physics.C_Grav_Accel(A, B)
        self.failUnless(np.allclose(Acc_vec_one, known_answer, 1.0e-6))
        
        
    def test_grav_accel_method_equal(self):
        part1 = Particle('a',[1.0, 1.0, 1.0], [1, 1, 1], 5.0)
        part2 = Particle('b',[1.00001,1.0000001,1.00001], [1,1,1], 5)
        part3 = Particle('c',[1.2e20, 1.2e21, 1.4e10], [1, 1, 1], 5.0)
        part4 = Particle('d',[1.01e-40, 1.3e-40, 1.4e-40], [1, 1, 1], 5.8e-100)
        part5 = Particle('e',[1.01e10, 1.44440000001110, 1.00000001], [1, 1, 1], 5.2)
        part6 = Particle('f',[-1.5, -1.5, -1.5], [-1, 1, 1], 5.3e24)
        base = PyGravity()
        self.failUnless(np.allclose(Physics.Grav_Accel(part1,part2), 
                                     Physics.C_Grav_Accel(part1,part2),
                                     1.0e-6))
                                     
        self.failUnless(np.allclose(Physics.Grav_Accel(part1,part3),
                                     Physics.C_Grav_Accel(part1,part3),
                                     1.0e-6))
                                     
        #self.failUnless(Physics.Grav_Accel(part1,part4).round(5) == Physics.C_Grav_Accel(part1,part4).round(5))
        self.failUnless(np.allclose(Physics.Grav_Accel(part1,part5),
                                     Physics.C_Grav_Accel(part1,part5),
                                     1.0e-6))
                                     
        self.failUnless(np.allclose(Physics.Grav_Accel(part1,part6),
                                     Physics.C_Grav_Accel(part1,part6),
                                     1.0e-6))
        
    def test_Total_Escape_Velocity(self):
        base = PyGravity()
        base.read_file('test_data.csv')
        escape_answer = 0.00003149801963613010526842131136
        escape = Physics.Total_Escape_Velocity(base.particle_list, base.particle_list[0])
        self.failUnless(round(escape,20) == round(escape_answer, 20))

    def _test_Physics_force_gravity_summation_for_one_particle(self):
        f = base.sum_Fg_one_particle(base.objects[0])
        self.failUnless(round_sig(f.x, 3 ) == round_sig(1.75*10**(-9), 3))
        self.failUnless(round_sig(f.y, 3 ) == round_sig(1.75*10**(-9), 3))
        self.failUnless(round_sig(f.z, 3 ) == round_sig(1.75*10**(-9), 3))

    def _test_partitcle_acceleration_3_object_harmonic_range(self):
        #this test setups 3 particles. one tiny, spaced eqidistance above the line of two
        #very heavy objects. The particle is supposed to bounce up and down across the line the
        # two heavy objects set on. This is testing to make sure the particle stays between
        # a maxima and minima and doesn't fly off in either direction.
        A = Particle('A',np.array(0,10.00,0), np.array(0,0,0), 1)
        B = Particle('B',np.array(-10,0,0), np.array(0,0,0), 10000000000)
        C = Particle('C',np.array(10,0,0), np.array(0,0,0), 10000000000)

        base = Physics()
        base.add_obj(A)
        base.add_obj(B)
        base.add_obj(C)
        for i in range(1000):
            base.apply_gravitational_acceleration(base.objects[0])
            base.objects[0].move
            self.failIf(base.objects[0].P.y > 12)
            self.failIf(base.objects[0].P.y < (-12))

            self.failUnless(base.objects[0].P.y < 12)
            self.failUnless(base.objects[0].P.y > (-12))
        
    def test_escaping(self):
        base = PyGravity()
        base.add_particle(self.part1)
        base.add_particle(self.part2)
        for i in range(100):
            base.step_all()
        self.failIf(Physics.escaping(base.particle_list) == [])
        
    def test_Proto_Accel(self):
        base = PyGravity()
        for part in self.part_list:
            base.add_particle(part)

        acc_accel_method = Physics.Grav_Accel(base.particle_list[0], 
                                              base.particle_list[1])
        acc_proto_method = Physics.Proto_Acc(base.particle_list[0], 
                                              base.particle_list[1])
        acc_proto_method = acc_proto_method * base.particle_list[1].m
        self.failUnless(np.allclose(acc_proto_method,
                                       acc_accel_method,
                                       1.0e-6))
        
    def _test_step_all_verlet_against_euler(self):
        #until Verlet method is fixed, leave unran
        base_verlet = PyGravity()
        base_euler = PyGravity()
        base_euler.set_time_interval(60)
        base_verlet.set_time_interval(60)
        base_euler.read_file('example_data.csv')
        base_verlet.read_file('example_data.csv')
        for i in range(10):
            base_verlet.step_all_verlet()
            base_euler.step_all()
            self.failUnless(np.allclose(base_euler.particle_list[0].P,
                                        base_verlet.particle_list[0].P,
                                        1.0e-6))
            print base_verlet.particle_list[0].P
            print base_euler.particle_list[0].P

    def test_step_verlet_one(self):
        #just check for errors
        Physics.step_verlet_one((self.part1,self.part2), 1)
        
    def test_step_verlet_two(self):
        #just check for errors
        Physics.step_verlet_one((self.part1,self.part2), 1)
        Physics.step_verlet_two((self.part1,self.part2), 1)
        
class Data_io_Class_Tests(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_read_csv(self):
        a = Particle('a', np.array(['1.1','1.2','0']), np.array(['0','0','0']), 50)
        d = Particle('d', np.array(['2.1','2.1','0']), np.array(['0','0','0']), 20)
        base = Data_IO.Reader()
        base.read_file('./test_data.csv')
        self.failUnless(base.objects[0].name == a.name)
        self.failUnless(np.array_equal(base.objects[0].P, a.P))
        self.failUnless(np.array_equal(base.objects[0].V, a.V))
        self.failUnless(base.objects[0].m == a.m)

    def test_read_xml_int(self):
        a = Particle('A', ['1','1','1'], ['1','0','0'], 50000000)
        
        base = Data_IO.Reader()
        base.read_file('./test_data.xml')
        self.failUnless(base.objects[0].name == a.name)
        self.failUnless(np.array_equal(base.objects[0].P, a.P))
        self.failUnless(np.array_equal(base.objects[0].V, a.V))
        self.failUnless(base.objects[0].m == a.m)
        

        
    def test_read_xml_float(self):
        d = Particle('D', [4.4, 4.4, 4.4], [0, 0, 0], 5.1e5)
        base = Data_IO.Reader()
        base.read_file('./test_data.xml')
        self.failUnless(base.objects[3].name == d.name)
        self.failUnless(np.array_equal(base.objects[3].P, d.P))
        self.failUnless(np.array_equal(base.objects[3].V, d.V))
        self.failUnless(base.objects[3].m == d.m)
        
        
class PyGravity_Class_Tests(unittest.TestCase):
    def setUp(self):
        self.A = Particle('A', np.array(['1']), np.array(['1']), 1)
        self.B = Particle('B', np.array(['1']), np.array(['1']), 1)
    
    def test_particle_add(self):
        base = PyGravity()
        base.add_particle(self.A)
        base.add_particle(self.B)
        self.failUnless(self.A.name == base.particle_list[0].name)
        self.failUnless(self.B.name == base.particle_list[1].name)
        
    def test_read_csv(self):
        a = Particle('a', np.array(['1.1','1.2','0']), np.array(['0','0','0']), 50)
        d = Particle('d', np.array(['2.1','2.1','0']), np.array(['0','0','0']), 20.0)
        base = PyGravity()
        base.read_file('./test_data.csv')
        self.failUnless(base.particle_list[0].name == a.name)
        self.failUnless(np.array_equal(base.particle_list[0].P, a.P))
        self.failUnless(np.array_equal(base.particle_list[0].V, a.V))
        self.failUnless(base.particle_list[0].m == a.m)
        
    def _test_step_all(self):
        '''
        .. todo:: Test the steps by comparting several itarations against
            an exact solution for various intervals and precision
        '''
        A = Particle('A', np.array(['1.0', '1.0','0']), np.array(['0', '0', '0' ]),500000000000)
        B = Particle('B', np.array(['5.0', '1.0', '0']), np.array(['0', '0', '0']), 500000000000)
        base = PyGravity()
        #base.set_fast()
        base.add_particle(A)
        base.add_particle(B)
        base.step_all()
        self.failUnless(base.particle_list[0].P.round(10) == np.array(['-1.084971875','1.0','0']).round(10))
        self.failUnless(base.particle_list[0].V.round(10) == np.array(['-2.084971875','0','0']).round(10))

        self.failUnless(base.particle_list[1].P.round(10) == np.array(['7.084971875','1.0','0']).round(10))
        self.failUnless(base.particle_list[1].V.round(10) == np.array(['2.084971875','0','0']).round(10))
        
        self.failIf(base.particle_list[0].P == np.array(['2.91442500000000', '1.00000000000000', '0']))
        self.failIf(base.particle_list[0].V == np.array(['-2.08557500000000', '0E-14', '0']))



#def run_test():
#    unittest.main()

if __name__ == "__main__":

    Round_test = unittest.TestLoader().loadTestsFromTestCase(Round_test)
    Part_test = unittest.TestLoader().loadTestsFromTestCase(Particle_Class_Tests)
    Physic_test = unittest.TestLoader().loadTestsFromTestCase(Physics_Class_Tests)
    Data_test = unittest.TestLoader().loadTestsFromTestCase(Data_io_Class_Tests)
    PyGrav_test = unittest.TestLoader().loadTestsFromTestCase(PyGravity_Class_Tests)
    alltest = unittest.TestSuite([Round_test,
                                  Part_test,
                                  Physic_test,
                                  Data_test,
                                  PyGrav_test])


    result = unittest.TextTestRunner(verbosity=2).run(alltest) 
    if result.errors != []:
        sys.exit('test errors\n')
    if result.failures != []:
        sys.exit('test failures\n')
