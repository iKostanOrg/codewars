#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

primes = [2, 3, 5, 7]


def is_prime(n):
	"""
	A function that checks if a given number n is a prime looping
	through it and, possibly, expanding the array/list of known
	primes only if/when necessary (ie: as soon as you check for a
	potential prime which is greater than a given threshold for each n, stop).
	:param n:
	:return:
	"""

	if n < 2:
		return False

	if n == 2:
		return True

	if n == 3:
		return True

	if n % 2 == 0 and n != 2:
		return False

	for i in range(3, int(n ** 0.5) + 1, 2):
		if is_prime(i) and i not in primes:
			primes.append(i)

		if n % i == 0:
			return False

	return True
