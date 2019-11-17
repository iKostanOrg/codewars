#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def alphabet_war(battlefield: str) -> str:
	"""
    A function that accepts battlefield string and
    returns letters that survived the nuclear strike.
    :param battlefield:
    :return:
    """
	result = ''

	if '#' not in battlefield:
		return ''.join(char for char in battlefield if char.isalpha() )
	else:
		result = clean_unsheltered(battlefield)
		result = clean_battlefield(result)

	return result


def clean_unsheltered(battlefield: str) -> str:
	"""
	Clean letters outside the shelter
	:param battlefield:
	:return:
	"""

	result = ''
	for i, char in enumerate(battlefield):

		if not char.isalpha():
			result += char

		if char.isalpha() and i != 0 and battlefield[i - 1] == '[' and battlefield[i + 1] == ']':
			result += char

	print('{} : {}'.format(battlefield, result))
	return result


def clean_battlefield(battlefield: str) -> str:
	"""
	Clean the battlefield and return only survived letters
	:param battlefield:
	:return:
	"""
	return


def contains_alpha(string: str) -> bool:

	for char in string:
		if char.isalpha():
			return True
	return False
