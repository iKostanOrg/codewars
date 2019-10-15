#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def logical_calc(array: list, op: str) -> bool:
	"""
    Calculates logical value of boolean array.

    Logical operations: AND, OR and XOR.

    Begins at the first value, and repeatedly
    apply the logical operation across the
    remaining elements in the array sequentially.

    :param array:
    :param op:
    :return:
    """

	logical = op.strip().upper()
	operators = ['AND', 'OR', 'XOR']

	# op param validation
	if logical not in operators:
		raise ValueError('ERROR: {} is not a valid operator. '
		                 'Please use one of the followings: {}'.
		                 format(op, operators))

	# AND
	if logical == operators[0]:
		return all(array)

	# OR
	if logical == operators[1]:
		return any(array)

	# XOR
	if logical == operators[2]:

		result = array[0]
		i = 1

		while i < len(array):

			tmp = array[i]

			if result == tmp:
				result = False
			else:
				result = True

			i = i + 1

		return result
