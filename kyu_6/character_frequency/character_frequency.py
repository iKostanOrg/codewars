#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def letter_frequency(text: str) -> list:
	"""
    return a list of tuples sorted by frequency with
    the most frequent letter first. Any letters with the
    same frequency are ordered alphabetically
    :param text:
    :return:
    """
	results = []
	chars = dict()
	text = text.lower()

	for c in text:
		if c.isalpha() and c not in chars:
			chars[c] = text.count(c)
			results.append((c, chars[c]))

	results = sort_list(results)
	return results


def sort_list(results) -> list:

	is_sorted = False

	while not is_sorted:
		is_sorted = True
		for i, el in enumerate(results):
			if i < (len(results) - 1):
				if results[i][1] < results[i + 1][1]:
					results[i], results[i + 1] = results[i + 1], results[i]
					is_sorted = False

				if results[i][1] == results[i + 1][1]:
					if results[i][0] > results[i + 1][0]:
						results[i], results[i + 1] = results[i + 1], results[i]
						is_sorted = False

	return results
