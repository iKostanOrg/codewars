#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.make_upper_case.make_upper_case import make_upper_case


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('MakeUpperCase')
class MakeUpperCaseTestCase(unittest.TestCase):
	"""
	Testing make_upper_case function
	"""

	def test_make_upper_case(self):
		"""
		Sample Tests for make_upper_case function
		:return:
		"""
		allure.dynamic.title("Testing make_upper_case function")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step("Pass lower case string and verify the output"):
			string = "hello"
			expected = "HELLO"

			print_log(string=string,
			          expected=expected)

			self.assertEqual(make_upper_case(string), expected)
