import unittest
from sum_of_two_lowest_int.sum_two_smallest_int import sum_two_smallest_numbers

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS, ARRAYS


class SumTwoSmallestNumbersTestCase(unittest.TestCase):

	def test_sum_two_smallest_numbers(self):
		"""
		Test sum_two_smallest_numbers function
		:return:
		"""
		self.assertEqual(
			sum_two_smallest_numbers([5, 8, 12, 18, 22]),
			13)

		self.assertEqual(
			sum_two_smallest_numbers([7, 15, 12, 18, 22]),
			19)

		self.assertEqual(
			sum_two_smallest_numbers([25, 42, 12, 18, 22]),
			30)
