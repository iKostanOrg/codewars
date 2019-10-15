import unittest
import allure
from utils.log_func import print_log
from kyu_8.multiply.multiply import multiply

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS, INTRODUCTION


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Math")
@allure.sub_suite("Unit Tests")
@allure.feature("Multiplication")
@allure.story('Multiply')
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

		allure.dynamic.title("'multiply' function verification")
		allure.dynamic.severity(allure.severity_level.MINOR)

		with allure.step("Assert (a * b) result"):
			a = 1
			b = 2
			expected = a * b

			print_log(a=a, b=b, expected=expected)

			self.assertEqual(expected,
			                 multiply(a, b))
