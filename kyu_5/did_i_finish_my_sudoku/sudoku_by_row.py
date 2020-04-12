#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def assert_sudoku_by_row(board: list) -> bool:
	for row in board:
		print(row)
		if len(row) != len(set(row)) or len(row) != len(board[0]):
			print('assert_sudoku_by_row #1')
			return False

		for i in row:
			if not isinstance(i, int):
				print('assert_sudoku_by_row #2')
				return False

	return True
