#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS STRINGS ARRAYS

import unittest
import allure
from utils.log_func import print_log
from kyu_6.duplicate_encoder.duplicate_encode import duplicate_encode


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Duplicate Encoder')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class DuplicateEncodeTestCase(unittest.TestCase):
	"""
	Testing duplicate_encode function
	"""

	def test_duplicate_encode(self):
		"""
		Testing duplicate_encode function
		with various test inputs
		:return:
		"""

		allure.dynamic.title("Testing duplicate_encode function")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		with allure.step("Enter test string and verify the output"):

			data = [
				("din", "((("),
				("recede", "()()()"),
				("Success", ")())())"),
				("(( @", "))((")
			]

			for string, expected in data:
				print_log(string=string, expected=expected)
				self.assertEqual(expected, duplicate_encode(string))
