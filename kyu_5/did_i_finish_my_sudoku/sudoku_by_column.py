#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def assert_sudoku_by_column(board: list) -> bool:
	row_length = len(board[0])
	for i in range(0, row_length):
		col = set()
		for row in board:
			col.add(row[i])
		if len(col) != row_length:
			print('assert_sudoku_by_column')
			return False

	return True
