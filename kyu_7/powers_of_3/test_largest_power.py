#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS LOOPS CONTROL FLOW BASIC LANGUAGE FEATURES FUNDAMENTALS MATHEMATICS NUMBERS

import unittest
import allure
from utils.log_func import print_log
from kyu_7.powers_of_3.largest_power import largestPower


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Flow Control")
@allure.story('Powers of 3')
class LargestPowerTestCase(unittest.TestCase):
	"""
	Testing largestPower function
	"""

	def test_largest_power(self):
		"""
		Testing largestPower function
		:return:
		"""

		allure.dynamic.title("Testing largestPower function")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		with allure.step("Pass an integer and verify the output"):
			n = 3
			expected = 0

			print_log(N=n, expected=expected)
			self.assertEqual(largestPower(n), expected)

		with allure.step("Pass an integer and verify the output"):
			n = 4
			expected = 1

			print_log(N=n, expected=expected)
			self.assertEqual(largestPower(n), expected)
