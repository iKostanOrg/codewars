def remove_smallest(numbers):
	"""
	Given an array of integers, remove the smallest value.
	Do not mutate the original array/list. If there are multiple
	elements with the same value, remove the one with a lower index.
	If you get an empty array/list, return an empty array/list.

    Don't change the order of the elements that are left.
	:param numbers:
	:return:
	"""
	new_array = []

	if len(numbers) > 0:
		min_num = min(numbers)
		min_i = numbers.index(min_num)

		for i in range(len(numbers)):
			if i != min_i:
				new_array.append(numbers[i])
	else:
		return numbers

	return new_array
