#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def feast(beast: str, dish: str) -> bool:
    """
    A function feast that takes the animal's name and
    dish as arguments and returns true or false to
    indicate whether the beast is allowed to bring the
    dish to the feast.

	Assume that beast and dish are always lowercase strings,
	and that each has at least two letters. beast and dish
	may contain hyphens and spaces, but these will not appear
	at the beginning or end of the string. They will not
	contain numerals.
    :param beast:
    :param dish:
    :return:
    """

    return beast[0] == dish[0] and beast[-1] == dish[-1]
