#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS FUNDAMENTALS NUMBERS

import unittest
import allure
from utils.log_func import print_log
from kyu_7.sum_of_powers_of_2.sum_of_powers_of_2 import powers


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Calculation")
@allure.story('Sum of powers of 2')
class SumOfPowerOfTwoTestCase(unittest.TestCase):
	"""
	Testing powers function
	"""

	def test_powers(self):
		"""
		The function powers takes a single parameter,
		the number n, and should return an array of unique numbers.
		:return:
		"""

		allure.dynamic.title("powers function should return "
		                     "an array of unique numbers")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step("Pass n = 1 and verify the output"):
			n = 1
			expected = [1]

			print_log(n=n, expected=expected)
			self.assertEqual(powers(n), expected)

		with allure.step("Pass n = 2 and verify the output"):
			n = 2
			expected = [2]

			print_log(n=n, expected=expected)
			self.assertEqual(powers(n), expected)

		with allure.step("Pass n = 4 and verify the output"):
			n = 4
			expected = [4]

			print_log(n=n, expected=expected)
			self.assertEqual(powers(n), expected)

		with allure.step("Pass n = 6 and verify the output"):
			n = 6
			expected = [2, 4]

			print_log(n=n, expected=expected)
			self.assertEqual(powers(n), expected)

		with allure.step("Pass n = 14 and verify the output"):
			n = 14
			expected = [2, 4, 8]

			print_log(n=n, expected=expected)
			self.assertEqual(powers(n), expected)

		with allure.step("Pass n = 32 and verify the output"):
			n = 32
			expected = [32]

			print_log(n=n, expected=expected)
			self.assertEqual(powers(n), expected)

		with allure.step("Pass n = 128 and verify the output"):
			n = 128
			expected = [128]

			print_log(n=n, expected=expected)
			self.assertEqual(powers(n), expected)

		with allure.step("Pass n = 512 and verify the output"):
			n = 512
			expected = [512]

			print_log(n=n, expected=expected)
			self.assertEqual(powers(n), expected)

		with allure.step("Pass n = 514 and verify the output"):
			n = 514
			expected = [2, 512]

			print_log(n=n, expected=expected)
			self.assertEqual(powers(n), expected)

		with allure.step("Pass n = 688 and verify the output"):
			n = 688
			expected = [16, 32, 128, 512]

			print_log(n=n, expected=expected)
			self.assertEqual(powers(n), expected)

		with allure.step("Pass n = 8197 and verify the output"):
			n = 8197
			expected = [1, 4, 8192]

			print_log(n=n, expected=expected)
			self.assertEqual(powers(n), expected)

		with allure.step("Pass n = 1966 and verify the output"):
			n = 1966
			expected = [2, 4, 8, 32, 128, 256, 512, 1024]

			print_log(n=n, expected=expected)
			self.assertEqual(powers(n), expected)

		with allure.step("Pass n = 134217736 and verify the output"):
			n = 134217736
			expected = [8, 134217728]

			print_log(n=n, expected=expected)
			self.assertEqual(powers(n), expected)

		with allure.step("Pass n = 140737488355330 and verify the output"):
			n = 140737488355330
			expected = [2, 140737488355328]

			print_log(n=n, expected=expected)
			self.assertEqual(powers(n), expected)

		with allure.step("Pass n = 35184372088896 and verify the output"):
			n = 35184372088896
			expected = [64, 35184372088832]

			print_log(n=n, expected=expected)
			self.assertEqual(powers(n), expected)

		with allure.step("Pass n = 9007199254740991 and verify the output"):
			n = 9007199254740991
			expected = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192,
			            16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152,
			            4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456,
			            536870912, 1073741824, 2147483648, 4294967296, 8589934592, 17179869184,
			            34359738368, 68719476736, 137438953472, 274877906944, 549755813888,
			            1099511627776, 2199023255552, 4398046511104, 8796093022208, 17592186044416,
			            35184372088832, 70368744177664, 140737488355328, 281474976710656, 562949953421312,
			            1125899906842624, 2251799813685248, 4503599627370496]

			print_log(n=n, expected=expected)
			self.assertEqual(powers(n), expected)
