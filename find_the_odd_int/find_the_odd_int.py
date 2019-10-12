def find_it(seq) -> int:
	"""
	Given an array, find the int that
	appears an odd number of times.
	:param seq:
	:return:
	"""
	pares = dict()

	for n in seq:
		if n not in pares:
			pares[n] = 1
		else:
			pares[n] = pares.get(n) + 1

	for key in pares.keys():
		if pares.get(key) % 2 > 0:
			return key
