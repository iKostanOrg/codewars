#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from math import factorial


def diagonal(n, p):
	# n choose p, returns int
	return factorial(n + 1) // (factorial(n - p) * factorial(p + 1))
