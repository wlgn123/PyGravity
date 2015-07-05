import unittest
from PyGravity import round_sig

class Round_test(unittest.TestCase):
	def setUp(self):
		pass

	def test_rounding_domain(self):
		a = 0
		self.failUnless(round_sig(a, 1) == 0)

	def test_neg_numbers(self):
		a = -1.2
		self.failUnless(round_sig(a,2) == -1.2)




def test_round_sig():
	unittest.main()

if __name__ == "__main__":
	test_round_sig()
