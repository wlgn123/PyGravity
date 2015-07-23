import unittest
from PyGravity import PyGravity, round_sig, Vector, Particle, Physics, Data_IO
from decimal import *
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


class Vector_Class_Tests(unittest.TestCase):
	def setUp(self):
		getcontext().prec = 400
		self.A = Vector([1,2,3])
		self.B = Vector([1,1,1])
		self.C = Vector([2.334e+20, 3.123456e+20])
		self.D = Vector([4.334e+20, 2.123456e+20])
		self.E = Vector(['1.2131313131231231231231231231231231231123123123123',
						 '2.213123123123131231231312312312312312123'])
		self.F = Vector(['1.2131313131231231231231231231231231231123123123121', 
						 '2.213123123123131231231312312312312312121'])
		self.H = Vector(['1.00000000000000000000000000000000000000000000000001',
						 '0'])
		self.I = Vector(['1.00000000000000000000000000000000000000000000000002',
						 '0'])
		self.L = Vector(['1.1111111111111111111111111111111111111222'])
		self.M = Vector(['1.2345679133333333333333333333333333333456543211084'])

		self.Z = Vector([0,0])

	def test_indexing(self):
		self.failUnless(self.A[0] == self.B[1])
		self.failIf(self.A[2] == self.B[0])

	def test_equalities(self):
		self.failUnless(self.A == self.A)
		self.failUnless((self.B + self.A) == (self.B + self.A))
		self.failIf(self.A == self.B)


	def test_array_match(self):
		self.failIf(self.E.array_mismatch(self.F))
		self.failUnless(self.F.array_mismatch(Vector(['1'])))

	def test_more_addition(self):
		self.failUnless((self.E+self.F) == (self.E+self.F))

	def test_big_equalities(self):
		self.failUnless(self.C == self.C)
		self.failIf(self.C == self.D)

	def test_equality_precise(self):
		self.failUnless(self.E == self.E)
		self.failIf(( self.E- self.F) == self.Z)
		self.failUnless(self.I - self.I  == self.Z)
		self.failIf(self.H + self.H == self.H + self.I)

	def test_array_match(self):
		self.assertRaises(ValueError, self.A.__eq__, self.E )
		
	def test_scalar_mul(self):
		new_vec = self.L * 1.111111122
		self.failUnless(new_vec.round(10) == self.M.round(10))
		
	def test_rounding(self):
		self.failUnless(self.E.round(2) == self.F.round(2))
		self.failUnless(self.E.round(4.1) == self.F.round(4.2))


	def test_magnitude(self):
		a = Vector(['2','4','4'])
		ans_a = Decimal('6')
		self.failUnless(a.magnitude() == ans_a)

		b = Vector(['2.0000000000000000000000002e+21',
					'4.4444444444444444444444444444e+20',
					'4.111111111111111111111e+20'])
		ans_b = Decimal('2089627528981311829491.1651755792781224241378604149887198762611497762517918313595066680613531301073141511728460949328602506908336809936538778205045521740966301651816135598736415281509427651835812164324')
		self.failUnless(round_sig(b.magnitude(),10) 
					    == round_sig(ans_b,10))

		c = Vector(['3','4'])
		self.failUnless(c.magnitude() == Decimal('5'))

	def test_vector_unit(self):
		a = Vector(['1.12','2.34','3.45'])
		ans_a = Vector(['0.259467195511802019559694863263',
					    '0.54210110490858636229436248217',
					    '0.79925162903189014953656'])
		self.failUnless(a.unit().round(10) == ans_a.round(10))

		b = Vector(['2','4','4'])
		ans_b = Vector(['1','2','2'])
		self.failUnless(b.unit() * 3 == ans_b)

class Particle_Class_Tests(unittest.TestCase):
	def setUp(self):
		pass

	def test_particle_creation(self):
		a = Particle('a',Vector([1,2,3]),
						 Vector([1,1,1]), 
						 Vector([55.5]))
		self.failUnless(hasattr(a, 'P'))
		self.failUnless(hasattr(a, 'V'))
		self.failUnless(hasattr(a, 'm'))
		self.failUnless(a.name == 'a')

	def test_particle_motion(self):
		a = Particle('a', Vector(['1','2','3']),
			              Vector(['1','1','1']), 
			              Vector(['55.5']))
		a.move(1)
		V = Vector([1,1,1])
		P = Vector([2,3,4])
		self.failUnless(P== a.P)

	def test_particle_motion2(self):
		a = Particle('a',Vector([1.1,2.1,3.0]),
						 Vector([1.1,2.1,3.0]),
						 Vector([55.5]))
		Accel = Vector([2,2,-4])
		Ans = Vector([3.1, 4.1, -1.0])
		a.accelerate(Accel,1)
		self.failUnless(Ans == a.V)

	def test_particle_acceleration(self):
		a = Particle('a',Vector([1, 1, 1]), 
						 Vector([1,1,1]), 
						 Vector([44]))
		Acc = Vector([3, 3, -1])
		V_ans = Vector([4, 4, 0])
		P_ans = Vector([5, 5, 1])
		a.accelerate(Acc,1)
		self.failUnless(V_ans == a.V)
		a.move(1)
		self.failUnless(P_ans == a.P)

class Physics_Class_Tests(unittest.TestCase):
	def setUp(self):
		self.part1 = Particle('a',Vector([1,1,1]),
								  Vector([1,1,1]), 
								  Vector([5]))
		self.part2 = Particle('b',Vector([2*10**42,1*10**42,3*10**42]), 
								  Vector([2.3, 1.2, 4.2]), 
								  Vector([5*10**6]))
		part1 = Particle('aa',Vector(['1.00009','1.000009','1.000009']), 
							  Vector(['1.09','1.09','1.09']), 
							  Vector(['5']))
		part2 = Particle('b',Vector([2,2,2]), 
							 Vector([2.3, 1.2, 4.2]), 
							 Vector([10]))
		part3 = Particle('c',Vector(['1.2e20','1.2e21','1.4e10']), 
							 Vector(['1','1','1']), 
							 Vector(['5']))
		part4 = Particle('d',Vector(['1.01e-40','1.3e-40','1.4e-40']), 
						     Vector(['1','1','1']), 
						     Vector(['5.8e-100']))
		part5 = Particle('e',Vector(['1.01e10','1.44440000001110',
									 '1.00000000000001']), 
						     Vector(['1','1','1']), 
						     Vector(['5.2']))
		part6 = Particle('f',Vector(['1.5','-1.2','-1.5']), 
							 Vector(['1','1','1']), 
							 Vector(['5.3e48']))
		self.part_list = [part1, part2, part3, part4, part5, part6]



	def test_Physics_Grav_Force(self):
		part1 = Particle('a',Vector(['1','1','1']), 
							 Vector(['1','1','1']), 
							 Vector(['5.0']))
		part2 = Particle('b',Vector(['2','2','2']), 
							 Vector(['2.3', '1.2', '4.2']), 
							 Vector(['10']))
		answer = Vector(['6.42e-10', '6.42e-10','6.42e-10 '])
		force_vec = Physics.Grav_Force(part1, part2)
		self.failUnless(answer.round(2) == force_vec.round(2) )
		
	def test_force_of_gravity_magnitude_against_precomputed_answer(self):
		part1 = Particle('a',Vector(['1.0','1.0','1.0']), 
							 Vector(['0','0','0']), 
							 Vector(['5.0e10']))
		part2 = Particle('b',Vector(['11.0','1.0','1.0']), 
							 Vector(['0','0','0']), Vector(['5.0e10']))
		force_vec = Physics.Grav_Force(part1, part2)
		self.failUnless(force_vec.magnitude() == 1668460000)

	def test_grav_accel_against_known_answer(self):
		A = Particle('a',Vector(['1','1','1']), 
						 Vector([1,1,1]), Vector(['5']))
		B = Particle('b',Vector(['2','2','2']), 
						 Vector([1,1,1]), Vector(['10']))
		#the known_answer was calculated by hand and verified w/ wolfram|alpha
		known_answer = Vector(['1.28438e-10',
							   '1.28438e-10', '1.28438e-10'])
		self.failUnless(known_answer.round(5) == 
						Physics.Grav_Accel(A,B).round(5))
		
		part6 = Particle('f',Vector(['1.5','-1.2','-1.5']), 
							 Vector(['1','1','1']), Vector(['5.3e20']))
		known_answer_part_6 = Vector(['4.6299417e8',
									  '-2.0371799e9','-2.3149771e9'])
		#self.failUnless(known_answer_part_6.round(3) == Physics.Grav_Accel(A,part6).round(3))
		
	def test_Grav_Accel(self):
		part1 = Particle('a',Vector(['1.0','1.0','1.0']), 
							 Vector([1,1,1]), Vector(['5.0']))
		
		Acceleration_answer = Vector(['6.42e-10', 
									  '6.42e-10',
									  '6.42e-10' ]) * (1/part1.m[0])
		Acc_Vector_one = (Physics.Grav_Force(part1, self.part_list[1]) * (1/part1.m[0])).round(4)
		Acc_Vector_two = Physics.Grav_Accel(part1, self.part_list[1]).round(4)
		self.failUnless(Acc_Vector_one == Acceleration_answer)
		self.failUnless(Acc_Vector_two == Acceleration_answer)
		
		for i in self.part_list:
			self.failUnless((Physics.Grav_Force(part1, i) * (1/part1.m[0])).round(4) 
							 == Physics.Grav_Accel(part1, i).round(4))
		
	def test_grav_accel_extension(self):
		A = Particle('a',Vector(['1.0','1.0','1.0']), Vector([1,1,1]), Vector(['5.0']))
		B = Particle('b',Vector(['2.0','2.0','2.0']), Vector([1,1,1]), Vector(['10.0']))
		#the known_answer was calculated by hand and verified w/ wolfram|alpha
		known_answer = Vector(['1.28438e-10', '1.28438e-10', '1.28438e-10'])
		Acc_Vector_one = Physics.C_Grav_Accel(A, B).round(5)
		self.failUnless(Acc_Vector_one == known_answer.round(5))
		
		
	def test_grav_accel_method_equal(self):
		part1 = Particle('a',Vector(['1.0','1.0','1.0']), Vector(['1','1','1']), Vector(['5.0']))
		part2 = Particle('b',Vector(['1.00001','1.0000001','1.00001']), Vector(['1','1','1']), Vector(['5']))
		part3 = Particle('c',Vector(['1.2e20','1.2e21','1.4e10']), Vector(['1','1','1']), Vector(['5.0']))
		part4 = Particle('d',Vector(['1.01e-40','1.3e-40','1.4e-40']), Vector(['1','1','1']), Vector(['5.8e-100']))
		part5 = Particle('e',Vector(['1.01e10','1.44440000001110','1.00000000000001']), Vector(['1','1','1']), Vector(['5.2']))
		part6 = Particle('f',Vector(['-1.5','-1.5','-1.5']), Vector(['-1','1','1']), Vector(['5.3e24']))
		base = PyGravity()
		base.set_precision(200)
		print Physics.Grav_Accel(part1,part2).round(5)
		print  Physics.C_Grav_Accel(part1,part2).round(5)
		self.failUnless(Physics.Grav_Accel(part1,part2).round(5) == Physics.C_Grav_Accel(part1,part2).round(5))
		self.failUnless(Physics.Grav_Accel(part1,part3).round(5) == Physics.C_Grav_Accel(part1,part3).round(5))
		#self.failUnless(Physics.Grav_Accel(part1,part4).round(5) == Physics.C_Grav_Accel(part1,part4).round(5))
		self.failUnless(Physics.Grav_Accel(part1,part5).round(5) == Physics.C_Grav_Accel(part1,part5).round(5))
		self.failUnless(Physics.Grav_Accel(part1,part6).round(5) == Physics.C_Grav_Accel(part1,part6).round(5))
		
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
		A = Particle('A',Vector(0,10.00,0), Vector(0,0,0), 1)
		B = Particle('B',Vector(-10,0,0), Vector(0,0,0), 10000000000)
		C = Particle('C',Vector(10,0,0), Vector(0,0,0), 10000000000)

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

class Data_io_Class_Tests(unittest.TestCase):
	def setUp(self):
		pass
		
	def test_read_csv(self):
		a = Particle('a', Vector(['1.1','1.2','0']), Vector(['0','0','0']), Vector(['50']))
		d = Particle('d', Vector(['2.1','2.1','0']), Vector(['0','0','0']), Vector(['20']))
		base = Data_IO.Reader()
		base.read_file('./test_data.csv')
		self.failUnless(base.objects[0].name == a.name)
		self.failUnless(base.objects[0].P == a.P)
		self.failUnless(base.objects[0].V == a.V)
		self.failUnless(base.objects[0].m == a.m)

	def test_read_xml(self):
		a = Particle('A', Vector(['1','1','1']), Vector(['1','0','0']), Vector(['50000000']))
		d = Particle('D', Vector(['2.1','2.1','0']), Vector(['0','0','0']), Vector(['20']))
		base = Data_IO.Reader()
		base.read_file('./test_data.xml')
		self.failUnless(base.objects[0].name == a.name)
		self.failUnless(base.objects[0].P == a.P)
		self.failUnless(base.objects[0].V == a.V)
		self.failUnless(base.objects[0].m == a.m)

class PyGravity_Class_Tests(unittest.TestCase):
	def setUp(self):
		self.A = Particle('A', Vector(['1']), Vector(['1']), Vector(['1']))
		self.B = Particle('B', Vector(['1']), Vector(['1']), Vector(['1']))
	
	def test_particle_add(self):
		base = PyGravity()
		base.add_particle(self.A)
		base.add_particle(self.B)
		self.failUnless(self.A.name == base.particle_list[0].name)
		self.failUnless(self.B.name == base.particle_list[1].name)
		
	def test_read_csv(self):
		a = Particle('a', Vector(['1.1','1.2','0']), Vector(['0','0','0']), Vector(['50']))
		d = Particle('d', Vector(['2.1','2.1','0']), Vector(['0','0','0']), Vector(['20']))
		base = PyGravity()
		base.read_file('./test_data.csv')
		self.failUnless(base.particle_list[0].name == a.name)
		self.failUnless(base.particle_list[0].P == a.P)
		self.failUnless(base.particle_list[0].V == a.V)
		self.failUnless(base.particle_list[0].m == a.m)
		
	def test_step_all(self):
		'''
		.. todo:: Test the steps by comparting several itarations against
			an exact solution for various intervals and precision
		'''
		A = Particle('A', Vector(['1.0', '1.0','0']), Vector(['0', '0', '0' ]), Vector(['500000000000']))
		B = Particle('B', Vector(['5.0', '1.0', '0']), Vector(['0', '0', '0']), Vector(['500000000000']))
		base = PyGravity()
		#base.set_fast()
		base.add_particle(A)
		base.add_particle(B)
		base.step_all()
		self.failUnless(base.particle_list[0].P.round(10) == Vector(['-1.084971875','1.0','0']).round(10))
		self.failUnless(base.particle_list[0].V.round(10) == Vector(['-2.084971875','0','0']).round(10))

		self.failUnless(base.particle_list[1].P.round(10) == Vector(['7.084971875','1.0','0']).round(10))
		self.failUnless(base.particle_list[1].V.round(10) == Vector(['2.084971875','0','0']).round(10))
		
		self.failIf(base.particle_list[0].P == Vector(['2.91442500000000', '1.00000000000000', '0']))
		self.failIf(base.particle_list[0].V == Vector(['-2.08557500000000', '0E-14', '0']))



def run_test():
	unittest.main()

if __name__ == "__main__":
	run_test()

