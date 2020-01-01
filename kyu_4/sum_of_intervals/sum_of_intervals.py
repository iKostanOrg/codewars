def sum_of_intervals(intervals: list) -> int:
	"""
	Accepts an array of intervals, and returns
	the sum of all the interval lengths.

	Overlapping intervals should only be counted once.
	:param intervals:
	:return:
	"""

	intervals = remove_overlaps(intervals)
	results = list()

	for i in intervals:
		results.append(i[1] - i[0])

	return sum(results)


def remove_overlaps(intervals: list) -> list:
	"""
    Remove overlaps and duplicates
    :param intervals:
    :return:
    """

	is_clean = False
	while not is_clean:
		is_clean = True

		for index_i, i in enumerate(intervals):
			for index_b, b in enumerate(intervals):
				if index_b != index_i:
					is_clean = do_something(intervals, i, b)
					if not is_clean:
						break

	return intervals


def clean_interval(intervals, i, b) -> bool:

	if i[0] == b[0] and i[1] == b[1]:
		intervals.remove(b)
		return False

	if i[0] < b[0] < i[1] <= b[1]:
		intervals.append((i[0], b[1]))
		intervals.remove(i)
		intervals.remove(b)
		return False

	if b[0] < i[0] < b[1] <= i[1]:
		intervals.append((b[0], i[1]))
		intervals.remove(i)
		intervals.remove(b)
		return False

	if b[0] < i[0] < i[1] < b[1]:
		intervals.remove(i)
		return False

	if i[0] < b[0] < b[1] < i[1]:
		intervals.remove(b)
		return False

	if i[0] == b[0] and b[1] < i[1]:
		intervals.remove(b)
		return False

	if i[0] == b[0] and i[1] < b[1]:
		intervals.remove(i)
		return False

	return True
