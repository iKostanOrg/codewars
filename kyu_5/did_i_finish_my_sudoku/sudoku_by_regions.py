#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from utils.primes.primes_generator import gen_primes


def assert_sudoku_by_region(board: list) -> bool:
	"""
	Assert Sudoku by region

	:param board: Sudoku list
	:return: boolean value (is Sudoku done or not)
	"""
	row_length = len(board[0])

	step = 0
	for i in gen_primes():
		if row_length % i == 0:
			step = i
			break
	print('Step: {}'.format(step))

	start, end = 0, step

	# limit = (row_length // step)  # + 1 if step % 2 != 0 else 0
	# print('limit: {}'.format(limit))

	for t in range(0, step):
		print()
		for i in range(0, row_length, step):
			region = list()
			for a in range(i, i + step):
				print('a: {}, start: {}, end: {}'.format(a, start, end))
				row = board[a][start: end]
				for b in row:
					region.append(b)
			print(region)
			s_region = set(region)
			if len(s_region) != row_length:
				print(s_region)
				print('assert_sudoku_by_region')
				return False

		start, end = end, end + step

	return True
