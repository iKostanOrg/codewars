#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def assert_sudoku_by_row(board: list) -> bool:
	for row in board:
		if len(row) != len(set(row)):
			print('assert_sudoku_by_row')
			return False
	return True
