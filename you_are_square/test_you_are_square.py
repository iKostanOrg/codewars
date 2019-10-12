import unittest
from you_are_square.you_are_square import is_square

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS, MATH


class YouAreSquareTestCase(unittest.TestCase):
	"""
	Testing is_square function

	The tests will always use some integral number,
	so don't worry about that in dynamic typed languages.
	"""

	def test_is_square_negative_numbers(self):
		"""
		-1: Negative numbers cannot be square numbers
		:return:
		"""
		self.assertEqual(is_square(-1),
		                 False,
		                 "-1: Negative numbers cannot be square numbers")

	def test_is_square_zero(self):
		"""
		0 is a square number
		:return:
		"""
		self.assertEqual(is_square(0),
		                 True,
		                 "0 is a square number")

	def test_is_square_negative_test(self):
		"""
		3 is not a square number
		:return:
		"""
		self.assertEqual(is_square(3),
		                 False,
		                 "3 is not a square number")

	def test_is_square_four(self):
		self.assertEqual(is_square(4),
		                 True,
		                 "4 is a square number")

	def test_is_square_25(self):
		"""
		25 is a square number
		:return:
		"""
		self.assertEqual(is_square(25),
		                 True,
		                 "25 is a square number")

	def test_is_square_26(self):
		"""
		26 is not a square number
		:return:
		"""
		self.assertEqual(is_square(26),
		                 False,
		                 "26 is not a square number")
