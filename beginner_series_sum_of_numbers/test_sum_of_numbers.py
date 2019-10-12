import unittest
from beginner_series_sum_of_numbers.sum_of_numbers import get_sum

# FUNDAMENTALS, ALGORITHMS


class SumOfNumbersTestCase(unittest.TestCase):
	"""
	Testing get_sum function
	"""

	def test_get_sum_equal_numbers(self):
		"""
		a and b are equal
		:return:
		"""
		self.assertEqual(get_sum(1, 1), 1)

	def test_get_sum_positive_numbers(self):
		"""
		a an b are positive numbers
		:return:
		"""
		self.assertEqual(get_sum(0, 1), 1)
		self.assertEqual(get_sum(1, 0), 1)
		self.assertEqual(get_sum(1, 2), 3)

	def test_get_sum_negative_numbers(self):
		"""
		a or b is negative
		:return:
		"""
		self.assertEqual(get_sum(0, -1), -1)
		self.assertEqual(get_sum(-1, 0), -1)
		self.assertEqual(get_sum(-1, 2), 2)
