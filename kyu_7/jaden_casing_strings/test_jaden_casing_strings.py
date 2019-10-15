import unittest
import allure
from utils.log_func import print_log
from kyu_7.jaden_casing_strings.jaden_casing_strings import toJadenCase

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS, STRINGS, ARRAYS


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Jaden Casing Strings')
class JadenCasingStringsTestCase(unittest.TestCase):
	"""
	Testing toJadenCase function
	"""

	def test_to_jaden_case_positive(self):
		"""
		Simple positive test
		:return:
		"""
		allure.dynamic.title("Testing toJadenCase function (positive)")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step("Pass string and verify the output"):
			quote = "How can mirrors be real if our eyes aren't real"
			expected = "How Can Mirrors Be Real If Our Eyes Aren't Real"

			print_log(string=quote, expected=expected)

			self.assertEqual(toJadenCase(quote), expected)

	def test_to_jaden_case_negative(self):
		"""
		Simple negative test
		:return:
		"""

		allure.dynamic.title("Testing toJadenCase function (negative)")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step("Pass string and verify the output"):
			quote = "How can mirrors be real if our eyes aren't real"

			print_log(string=quote, expected=False)

			self.assertNotEqual(toJadenCase(quote), quote)
