#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS STRINGS STRING FORMATTING FORMATTING ALGORITHMS ARRAYS MATHEMATICS

import unittest
import allure
from utils.log_func import print_log
from kyu_7.always_perfect.check_root import check_root


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Always perfect')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class CheckRootTestCase(unittest.TestCase):
	"""
	Testing check_root function
	"""

	def test_check_root(self):
		"""
		Testing check_root function with various test inputs

		A function which takes numbers separated by commas
		in string format and returns the number which is a
		perfect square and the square root of that number.

		If string contains other characters than number or
		it has more or less than 4 numbers separated by comma
		function returns "incorrect input".

		If string contains 4 numbers but not consecutive it
		returns "not consecutive".
		:return:
		"""

		allure.dynamic.title("Testing check_root function")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		with allure.step("Enter test string and verify the output"):

			data = [
				('4,5,6,7', '841, 29'),
				('3,s,5,6', 'incorrect input'),
				('11,13,14,15', 'not consecutive'),
				('10,11,12,13,15', 'incorrect input'),
				('10,11,12,13', '17161, 131'),
				('*-3,-2,-1,0', 'incorrect input'),
			]

			for string, expected in data:
				print_log(string=string, expected=expected)
				self.assertEqual(expected, check_root(string))
