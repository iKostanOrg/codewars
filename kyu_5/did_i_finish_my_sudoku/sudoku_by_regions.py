#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def assert_sudoku_by_region(board: list) -> bool:
	row_length = len(board[0])
	start, end = 0, 3

	for t in range(0, 3):
		for i in range(0, 7, 3):

			region = set()
			for a in range(i, i + 3):
				row = board[a][start: end]
				for b in row:
					region.add(b)

			if len(region) != row_length:
				# print('assert_sudoku_by_region')
				return False

		start, end = end, end + 3

	return True
