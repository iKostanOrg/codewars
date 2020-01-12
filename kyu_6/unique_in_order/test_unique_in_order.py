#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS ADVANCED LANGUAGE FEATURES ALGORITHMS

import allure
import unittest
from utils.log_func import print_log
from kyu_6.unique_in_order.unique_in_order import unique_in_order


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Advanced Language Features")
@allure.sub_suite("Unit Tests")
@allure.feature("Algorithms")
@allure.story('Unique In Order')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class UniqueInOrderTestCase(unittest.TestCase):
	"""
	Testing the 'unique_in_order' function
	"""

	def test_unique_in_order(self):
		"""
		Testing the 'unique_in_order' function
		with various test data
		:return:
		"""

		allure.dynamic.title("Testing the 'unique_in_order' function")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		with allure.step("Pass test data and verify the output"):
			data = [
				('AAAABBBCCDAABBB',
				 ['A', 'B', 'C', 'D', 'A', 'B']),
				('ABBCcAD',
				 ['A', 'B', 'C', 'c', 'A', 'D']),
				([1, 2, 2, 3, 3],
				 [1, 2, 3])
			]

			for test_data, expected in data:
				print_log(iterable=test_data, expected=expected)
				self.assertEqual(expected, unique_in_order(test_data))
