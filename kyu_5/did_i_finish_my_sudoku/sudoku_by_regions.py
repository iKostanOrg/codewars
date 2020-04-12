#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/
from utils.primes.primes_generator import gen_primes


def assert_sudoku_by_region(board: list) -> bool:
	row_length = len(board[0])
	start, end = 0, 3

	step = 0
	for i in gen_primes():
		if row_length % i == 0:
			step = i
			break

	for t in range(0, step):
		# print()
		for i in range(0, row_length - step + 1 if step % 2 != 0 else 0, step):
			region = set()
			for a in range(i, i + step):
				row = board[a][start: end]
				for b in row:
					region.add(b)
			# print(region)
			if len(region) != row_length:
				# print('assert_sudoku_by_region')
				return False

		start, end = end, end + 3

	return True
