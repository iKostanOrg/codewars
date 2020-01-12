#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS

import unittest
import allure
from utils.log_func import print_log
from kyu_6.pyramid_array.pyramid_array import pyramid


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Pyramid Array')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class PyramidTestCase(unittest.TestCase):
	"""
	Testing 'pyramid' function
	"""

	def test_pyramid(self):
		"""
		The 'pyramid' function should return
		an Array of ascending length subarrays.

		Note: the subarrays should be filled with 1s.
		:return:
		"""

		allure.dynamic.title("Testing the 'pyramid' function")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		with allure.step("Pass zero"):
			n = 0
			expected = []

			print_log(n=n, expected=expected)

			self.assertEqual(pyramid(n), expected)

		with allure.step("Pass one"):
			n = 1
			expected = [[1]]

			print_log(n=n, expected=expected)

			self.assertEqual(pyramid(n), expected)

		with allure.step("Pass two"):
			n = 2
			expected = [[1], [1, 1]]

			print_log(n=n, expected=expected)

			self.assertEqual(pyramid(n), expected)

		with allure.step("Pass three"):
			n = 3
			expected = [[1], [1, 1], [1, 1, 1]]

			print_log(n=n, expected=expected)

			self.assertEqual(pyramid(n), expected)
