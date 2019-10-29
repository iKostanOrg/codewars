#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS LISTS DATA STRUCTURES ARRAYS


def save(sizes: list, hd: int) -> int:
	"""
	Your task is to determine how many files of the
	copy queue you will be able to save into your
	Hard Disk Drive.

	Input:
	Array of file sizes (0 <= s <= 100)
	Capacity of the HD (0 <= c <= 500)

	Output:
	Number of files that can be fully saved in the HD

	:param sizes:
	:param hd:
	:return:
	"""

	counter = 0
	total = 0

	for size in sizes:

		total += size
		counter += 1

		if total > hd:
			counter -= 1
			break

	return counter
