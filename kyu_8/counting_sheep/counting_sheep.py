#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def count_sheeps(arrayOfSheeps: list) -> int:
	"""
	Consider an array of sheep where some sheep
	may be missing from their place. We need a
	function that counts the number of sheep
	present in the array (true means present).

	Hint: Don't forget to check for bad values
	like null/undefined
	:param arrayOfSheeps:
	:return:
	"""
	return 0 if arrayOfSheeps is None \
		else arrayOfSheeps.count(True)
