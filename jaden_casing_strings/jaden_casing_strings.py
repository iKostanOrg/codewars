#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def toJadenCase(string):
	"""
	Convert strings to how they would
	be written by Jaden Smith. The strings
	are actual quotes from Jaden Smith,
	but they are not capitalized in the
	same way he originally typed them.

	Example:

		Not Jaden-Cased:
			"How can mirrors be real if
			our eyes aren't real"

		Jaden-Cased:
			"How Can Mirrors Be Real If
			Our Eyes Aren't Real"

	:param string:
	:return:
	"""
	list_string = string.split()

	for i in range(len(list_string)):
		list_string[i] = list_string[i].capitalize()

	new_string = ' '.join(list_string)

	return new_string
