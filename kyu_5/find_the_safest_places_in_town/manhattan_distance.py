#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def get_manhattan_distance(coord_a: tuple, coord_b: tuple) -> int:
	"""
	Manhattan distance:
	The distance between two points measured along axes at right angles.
	In a plane with p1 at (x1, y1) and p2 at (x2, y2), it is |x1 - x2| + |y1 - y2|.

	:param coord_a:
	:param coord_b:
	:return:
	"""
	manhattan_distance = abs(coord_a[0] - coord_b[0]) + abs(coord_a[1] - coord_b[1])
	# print('\na: {},\nb: {},\n{}'.format(coord_a, coord_b, manhattan_distance))
	return manhattan_distance
