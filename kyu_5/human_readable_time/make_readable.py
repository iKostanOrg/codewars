#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def make_readable(seconds: int) -> str:
	"""
    Write a function, which takes a non-negative integer
    (seconds) as input and returns the time in a
    human-readable format (HH:MM:SS)

	HH = hours, padded to 2 digits, range: 00 - 99
	MM = minutes, padded to 2 digits, range: 00 - 59
	SS = seconds, padded to 2 digits, range: 00 - 59

	The maximum time never exceeds 359999 (99:59:59)
    :param seconds:
    :return:
    """

	hours = seconds // (60 * 60)
	minutes = (seconds - (hours * 60 * 60)) // 60
	seconds = seconds - (hours * 60 * 60) - (minutes * 60)

	print('{}:{}:{}'.format(hours, minutes, seconds))

	if hours == 0:
		hours = '00'
	else:
		if len(str(hours)) > 1:
			hours = str(hours)
		else:
			hours = '0' + str(hours)

	if minutes == 0:
		minutes = '00'
	else:
		if len(str(minutes)) > 1:
			minutes = str(minutes)
		else:
			minutes = '0' + str(minutes)

	if seconds == 0:
		seconds = '00'
	else:
		if len(str(seconds)) > 1:
			seconds = str(seconds)
		else:
			seconds = '0' + str(seconds)

	result = '{}:{}:{}'.format(
		hours,
		minutes,
		seconds
	)

	return result
