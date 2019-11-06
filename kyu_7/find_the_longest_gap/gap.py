#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def gap(num: int) -> int:
	"""
	Returns the length of its longest
	binary gap.

	The function should return 0 if
	num doesn't contain a binary gap.
	:param num:
	:return:
	"""
	binary = "{0:b}".format(num)
	g_max = 0
	g_cur = 0

	for i, char in enumerate(binary):

		if binary[i:].count('1') == 0:
			break

		if char == '0':
			g_cur += 1
		else:
			g_cur = 0

		if g_cur > g_max:
			g_max = g_cur

	return g_max
