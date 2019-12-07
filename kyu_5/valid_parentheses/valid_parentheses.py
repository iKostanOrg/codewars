#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def valid_parentheses(string: str) -> bool:
	"""
	A function called that takes a string of parentheses,
	and determines if the order of the parentheses is valid.
	The function should return true if the string is valid,
	and false if it's invalid.
	:param string:
	:return:
	"""

	string = clean_up_string(string)

	if string == "" or not string:
		return True

	if string[0] != '(':
		return False

	if len(string) % 2 != 0:
		return False

	if string.count('(') != string.count(')'):
		return False

	string_list = list(s for s in string)

	while string_list:
		pair = False

		if string_list[0] == ')':
			return False

		for s in string_list[1:]:
			if string_list[0] + s == '()':
				del string_list[0]
				string_list.remove(s)
				pair = True
				break

		if not pair:
			return False

	return True


def clean_up_string(string: str) -> str:
	"""
	Cleaning up string from invalid chars
	:param string:
	:return:
	"""
	return ''.join(s for s in string if s == '(' or s == ')')
