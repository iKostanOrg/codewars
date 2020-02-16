#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS INTERVIEW QUESTIONS ARRAYS SORTING

import allure
import unittest
from utils.log_func import print_log
from kyu_5.moving_zeros_to_the_end.move_zeros import move_zeros


@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Moving Zeros To The End')
@allure.tag('ALGORITHMS', 'INTERVIEW QUESTIONS', 'ARRAYS', 'SORTING')
@allure.link(url='',
             name='Source/Kata')
class MoveZerosTestCase(unittest.TestCase):
	"""
	Testing move_zeros function
	"""

	def test_move_zeros(self):
		"""
		Test an algorithm that takes an array and moves all of the
		zeros to the end, preserving the order of the other elements.
		:return:
		"""

		allure.dynamic.title("Testing move_zeros function")
		allure.dynamic.severity(allure.severity_level.NORMAL)
		allure.dynamic.description_html('<h3>Codewars badge:</h3>'
		                                '<img src="https://www.codewars.com/users/myFirstCode'
		                                '/badges/large">'
		                                '<h3>Test Description:</h3>'
		                                "<p></p>")

		with allure.step("Enter test data (list) and verify the output"):
			test_data = [
				([1, 2, 0, 1, 0, 1, 0, 3, 0, 1], [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]),
				([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9],
				 [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
				(["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9],
				 ["a", "b", "c", "d", 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
				(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9],
				 ["a", "b", None, "c", "d", 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
				([0, 1, None, 2, False, 1, 0], [1, None, 2, False, 1, 0, 0]),
				(["a", "b"], ["a", "b"]),
				(["a"], ["a"]),
				([0, 0], [0, 0]),
				([0], [0]),
				([False], [False]),
				([], []),
			]

			for d in test_data:
				array = d[0]
				expected = d[1]
				print_log(array=array, expected=expected)
				self.assertEqual(expected, move_zeros(array))
