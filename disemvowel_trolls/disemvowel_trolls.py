def disemvowel(string):
	"""
	A function that takes a string and return
	a new string with all vowels removed.

	For example, the string "This website is
	for losers LOL!" would become "Ths wbst s fr lsrs LL!".

	Note: for this kata y isn't considered a vowel.
	:param string:
	:return:
	"""
	vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
	print(string)

	new_string = []

	for char in string:
		if char not in vowels:
			new_string.append(char)

	print(new_string)
	string = ''.join(new_string)
	print(string)

	return string
