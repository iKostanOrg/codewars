def tickets(people: list) -> str:
	"""
    Return YES, if Vasya can sell a ticket to every
    person and give change with the bills he has at
    hand at that moment. Otherwise return NO.
    :param people:
    :return:
    """
	print(people)

	vasya = list()

	for p in people:

		if p == 25:
			vasya.append(p)
			continue

		if p == 50 and 25 in vasya:
			del vasya[vasya.index(25)]
			vasya.append(p)
			continue

		if p == 100:
			if 25 in vasya and 50 in vasya:
				del vasya[vasya.index(25)]
				del vasya[vasya.index(50)]
				vasya.append(p)
				continue

			if vasya.count(25) >= 3:
				i = 3
				while i > 0:
					del vasya[vasya.index(25)]
					i -= 1
				vasya.append(p)
				continue

		return 'NO'

	return "YES"
