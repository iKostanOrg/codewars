#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def calculate(s: str) -> str:
	CONVERSION = {
		'plus': '+',
		'minus': '-',
	}

	s = s.lower()
	for key in CONVERSION:
		if key in s:
			s = s.replace(key, CONVERSION[key])

	return str(eval(s))
