import unittest
from multiply.multiply import multiply

# FUNDAMENTALS, INTRODUCTION


class MultiplyTestCase(unittest.TestCase):
	"""
	Testing multiply function
	"""

	def test_multiply(self):
		"""
        Verify that multiply function
		returns correct result
		:return:
		"""
		a = 1
		b = 2
		expected = a * b
		self.assertEqual(expected, multiply(a, b))
