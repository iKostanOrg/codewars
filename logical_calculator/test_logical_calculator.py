#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS ARRAYS

import unittest
import allure
from utils.log_func import print_log
from logical_calculator.logical_calculator import logical_calc


@allure.epic('Codewars')
@allure.parent_suite('Fundamentals')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Logical Calculator')
class LogicalCalculatorTestCase(unittest.TestCase):
	"""
	Testing logical_calc function
	"""

	def test_logical_calc_and(self):
		"""
		And (∧) is the truth-functional
		operator of logical conjunction

		The and of a set of operands is true
		if and only if all of its operands are true.

		Source:
		https://en.wikipedia.org/wiki/Logical_conjunction

		:return:
		"""
		allure.dynamic.title("AND logical operator")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step("Pass an array with 2 members (negative)"):
			lst = [True, False]
			operator = 'AND'
			expected = False

			print_log(list=lst,
			          operator=operator,
			          expected=expected)

			self.assertEqual(logical_calc(lst, operator), expected)

		with allure.step("Pass an array with 3 members (negative)"):
			lst = [True, True, False]
			operator = 'AND'
			expected = False

			print_log(list=lst,
			          operator=operator,
			          expected=expected)

			self.assertEqual(logical_calc(lst, operator), expected)

		with allure.step("Pass an array with 3 members (negative)"):
			lst = [False, False, False]
			operator = 'AND'
			expected = False

			print_log(list=lst,
			          operator=operator,
			          expected=expected)

			self.assertEqual(logical_calc(lst, operator), expected)

		with allure.step("Pass an array with 3 members (positive)"):
			lst = [True, True, True]
			operator = 'AND'
			expected = True

			print_log(list=lst,
			          operator=operator,
			          expected=expected)

			self.assertEqual(logical_calc(lst, operator), expected)

		with allure.step("Pass large array (negative)"):
			lst = [False, False, False, False, True, True, False, True,
			       True, False, False, True, True, False, False, False,
			       False, True, True, False, True, False, False, True,
			       True, True, False, True, True, False, False, False,
			       False, False, False, True, True, True, True, False,
			       True, True, False, True, True, False, False, True,
			       False, False]
			operator = 'AND'
			expected = False

			print_log(list=lst,
			          operator=operator,
			          expected=expected)

			self.assertEqual(logical_calc(lst, operator), expected)

	def test_logical_calc_or(self):
		"""
		In logic and mathematics, or is the
		truth-functional operator of (inclusive)
		disjunction, also known as alternation.

		The or of a set of operands is true if
		and only if one or more of its operands is true.

		Source:
		https://en.wikipedia.org/wiki/Logical_disjunction

		:return:
		"""

		allure.dynamic.title("OR logical operator")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step('Pass an array with 2 members (positive)'):
			lst = [True, False]
			operator = 'OR'
			expected = True

			print_log(list=lst,
			          operator=operator,
			          expected=expected)

			self.assertEqual(logical_calc(lst, operator), expected)

		with allure.step('Pass an array with 3 members (positive)'):
			lst = [True, True, False]
			operator = 'OR'
			expected = True

			print_log(list=lst,
			          operator=operator,
			          expected=expected)

			self.assertEqual(logical_calc(lst, operator), expected)

		with allure.step('Pass an array with 3 members (negative)'):
			lst = [False, False, False]
			operator = 'OR'
			expected = False

			print_log(list=lst,
			          operator=operator,
			          expected=expected)

			self.assertEqual(logical_calc(lst, operator), expected)

		with allure.step('Pass large array (positive)'):
			lst = [False, True, True, False, False, False, True, False,
			       False, False, False, True, True, False, False, False,
			       True, False, False, True, True, True, True, True, False,
			       True, True, True, False, True, False, False, True, True,
			       True, True, True, True, False, True, False, True, False,
			       True, False, True, False, True, True, True]
			operator = 'OR'
			expected = True

			print_log(list=lst,
			          operator=operator,
			          expected=expected)

			self.assertEqual(logical_calc(lst, operator), expected)

	def test_logical_calc_xor(self):
		"""
		Exclusive or or exclusive disjunction is a
		logical operation that outputs true only when
		inputs differ (one is true, the other is false).

		XOR outputs true whenever the inputs differ:

		Source:
		https://en.wikipedia.org/wiki/Exclusive_or
		:return:
		"""

		allure.dynamic.title("XOR logical operator")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step('Pass an array with 2 members (positive)'):
			lst = [True, False]
			operator = 'OR'
			expected = True

			print_log(list=lst,
			          operator=operator,
			          expected=expected)

			self.assertEqual(logical_calc(lst, operator), expected)

		with allure.step('Pass an array with 3 members (negative)'):
			lst = [True, True, False]
			operator = 'XOR'
			expected = False

			print_log(list=lst,
			          operator=operator,
			          expected=expected)

			self.assertEqual(logical_calc(lst, operator), expected)

		with allure.step('Pass medium size array'):
			lst = [False, False, True, True, False, False, False, False, True]
			operator = 'XOR'
			expected = True

			print_log(list=lst,
			          operator=operator,
			          expected=expected)

			self.assertEqual(expected, logical_calc(lst, operator))

		with allure.step('Pass large size array #1'):
			lst = [False, False, True, False, False, True, True,
			       True, False, False, True, False, False, False,
			       False, True, False, True, False, False, True,
			       False, False, True, True, True, False, False,
			       False, False, True, False, False, False, False,
			       False, True, False, False, False, True, True,
			       False, True, False, True, False, False, True, False]
			operator = 'XOR'
			expected = False

			print_log(list=lst,
			          operator=operator,
			          expected=expected)

			self.assertEqual(expected, logical_calc(lst, operator))

		with allure.step('Pass large size array #2'):
			lst = [True, True, False, False, False, True, True, False,
			       False, True, False, False, True, False, False, True,
			       True, True, True, True, True, False, False, False,
			       False, True, True, False, False, True, True, True,
			       True, False, True, True, False, False, False, True,
			       False, True, False, True, False, False, True, False,
			       True, True]
			operator = 'XOR'
			expected = False

			print_log(list=lst,
			          operator=operator,
			          expected=expected)

			self.assertEqual(expected, logical_calc(lst, operator))
