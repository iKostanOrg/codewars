import unittest
import allure
from kyu_7.sum_of_two_lowest_int.sum_two_smallest_int import sum_two_smallest_numbers

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS, ARRAYS


@allure.epic('7 kyu')
@allure.parent_suite('Fundamentals')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Sum of two lowest positive integers')
class SumTwoSmallestNumbersTestCase(unittest.TestCase):

	def test_sum_two_smallest_numbers(self):
		"""
		Test sum_two_smallest_numbers function
		The function should return the sum of
		the two lowest positive numbers
		:return:
		"""
		allure.dynamic.title("Two smallest numbers in the start of the list")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		with allure.step(""):
			self.assertEqual(
				sum_two_smallest_numbers([5, 8, 12, 18, 22]),
				13)

		with allure.step("Two smallest numbers in the start/middle of the list"):
			self.assertEqual(
				sum_two_smallest_numbers([7, 15, 12, 18, 22]),
				19)

		with allure.step("Two smallest numbers in the middle of the list"):
			self.assertEqual(
				sum_two_smallest_numbers([25, 42, 12, 18, 22]),
				30)
