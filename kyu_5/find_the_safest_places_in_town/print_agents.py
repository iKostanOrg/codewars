#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def print_map(agents: list, n: int, expected: list):
	"""
	Use for debug purposes only. Prints city map with agents (*)
	and expected results (longest distance as +) on it.

	:param agents: is an array of agent coordinates
	:param n: defines the size of the city that Bassi needs to hide in,
			  in other words the side length of the square grid
	:param expected: expected results
	:return:
	"""
	empty = ' |'
	agent = '*|'
	longest = '+|'

	for col in range(0, n):
		temp = "|"
		for row in range(0, n):
			if (row, col) in agents:
				temp += agent
			elif (row, col) in expected:
				temp += longest
			else:
				temp += empty
		print(temp)
