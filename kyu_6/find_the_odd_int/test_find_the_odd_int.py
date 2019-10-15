import unittest
import allure
from utils.log_func import print_log
from kyu_6.find_the_odd_int.find_the_odd_int import find_it

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS


@allure.epic('6 kyu')
@allure.parent_suite('Fundamentals')
@allure.suite("Advanced Language Features")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Find the odd int')
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

		allure.dynamic.title("Find the int that appears "
		                     "an odd number of times")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		with allure.step("Assert the result"):
			lst = [20, 1, -1, 2, -2, 3, 3, 5, 5,
			       1, 2, 4, 20, 4, -1, -2, 5]
			expected = 5

			print_log(list=lst, expected=expected)

			self.assertEqual(find_it(lst), expected)
