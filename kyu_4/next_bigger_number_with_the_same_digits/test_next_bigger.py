#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# REFACTORING NUMBERS STRINGS INTEGERS

import allure
import unittest
import pytest
from utils.log_func import print_log
from kyu_4.next_bigger_number_with_the_same_digits.next_bigger import next_bigger


@allure.epic("4 kyu")
@allure.parent_suite('Competent')
@allure.suite("Numbers")
@allure.sub_suite("Unit Tests")
@allure.feature("Integers")
@allure.story("Next bigger number with the same digits")
@allure.tag('REFACTORING', 'NUMBERS', 'STRINGS', 'INTEGERS')
@allure.link(url='https://www.codewars.com/kata/55983863da40caa2c900004e/train/python',
             name='Source/Kata')
@pytest.mark.skip(reason="The solution is not ready")
class NextBiggerTestCase(unittest.TestCase):

	def test_next_bigger(self):
		"""
		Testing next_bigger function

		You have to test a function that takes a positive integer
		number and returns the next bigger number formed by the same digits:

		12 ==> 21
		513 ==> 531
		2017 ==> 2071

		If no bigger number can be composed using those digits, return -1:
		"""

		allure.dynamic.title("Testing next_bigger function")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step("Enter an integer and "
		                 "calculate the result"):
			data = [
				(12, 21),
				(513, 531),
				(2017, 2071),
				(414, 441),
				(144, 414),
			]

			for d in data:
				n = d[0]
				expected = d[1]

				print_log(n=n,
				          expected=expected)

				self.assertEqual(expected,
				                 next_bigger(n))
