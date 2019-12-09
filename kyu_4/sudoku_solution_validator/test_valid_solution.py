#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS DATA STRUCTURES VALIDATION

import allure
import unittest
from utils.log_func import print_log
from kyu_4.sudoku_solution_validator.valid_solution import validSolution


@allure.epic('4 kyu')
@allure.parent_suite('Competent')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Validation")
@allure.story('Sudoku Solution Validator')
class ValidSolutionTestCase(unittest.TestCase):
	"""
	Testing validSolution function
	"""

	def test_valid_solution(self):
		"""
		Test a function validSolution/ValidateSolution/valid_solution()
		that accepts a 2D array representing a Sudoku board, and returns
		true if it is a valid solution, or false otherwise. The cells of
		the sudoku board may also contain 0's, which will represent empty
		cells. Boards containing one or more zeroes are considered to be
		invalid solutions.

		The board is always 9 cells by 9 cells, and every
		cell only contains integers from 0 to 9.
		:return:
		"""

		allure.dynamic.title("Testing validSolution")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step("Enter test list and verify the output"):
			test_data = [
				([[5, 3, 4, 6, 7, 8, 9, 1, 2],
				  [6, 7, 2, 1, 9, 5, 3, 4, 8],
				  [1, 9, 8, 3, 4, 2, 5, 6, 7],
				  [8, 5, 9, 7, 6, 1, 4, 2, 3],
				  [4, 2, 6, 8, 5, 3, 7, 9, 1],
				  [7, 1, 3, 9, 2, 4, 8, 5, 6],
				  [9, 6, 1, 5, 3, 7, 2, 8, 4],
				  [2, 8, 7, 4, 1, 9, 6, 3, 5],
				  [3, 4, 5, 2, 8, 6, 1, 7, 9]], True),

				([[5, 3, 4, 6, 7, 8, 9, 1, 2],
				  [6, 7, 2, 1, 9, 0, 3, 4, 9],
				  [1, 0, 0, 3, 4, 2, 5, 6, 0],
				  [8, 5, 9, 7, 6, 1, 0, 2, 0],
				  [4, 2, 6, 8, 5, 3, 7, 9, 1],
				  [7, 1, 3, 9, 2, 4, 8, 5, 6],
				  [9, 0, 1, 5, 3, 7, 2, 1, 4],
				  [2, 8, 7, 4, 1, 9, 6, 3, 5],
				  [3, 0, 0, 4, 8, 1, 1, 7, 9]], False)]

			for data in test_data:

				board = data[0]
				expected = data[1]
				print_log(board=board,
				          expected=expected)

				self.assertEqual(expected,
				                 validSolution(board))
