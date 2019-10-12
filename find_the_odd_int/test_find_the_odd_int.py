import unittest
from find_the_odd_int.find_the_odd_int import find_it


# FUNDAMENTALS


class FindTheOddIntTestCase(unittest.TestCase):
	"""
	Testing find_it function
	"""

	def test_something(self):
		"""
		Sample testing.
		Expected result is 5
		:return:
		"""

		lst = [20, 1, -1, 2, -2, 3, 3, 5, 5,
		       1, 2, 4, 20, 4, -1, -2, 5]
		self.assertEqual(find_it(lst), 5)
