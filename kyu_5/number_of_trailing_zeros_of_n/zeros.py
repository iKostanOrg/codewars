#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def zeros(n):
    """
    A program that will calculate the number of
    trailing zeros in a factorial of a given number.

    N! = 1 * 2 * 3 * ... * N

    For more info, see: http://mathworld.wolfram.com/Factorial.html

	A simple way is to calculate floor(n/5). For example, 7! has
	one 5, 10! has two 5s. It is done yet, there is one more thing
	to consider. Numbers like 25, 125, etc have more than one 5.

	For example if we consider 28!, we get one extra 5 and number of 0s become 6.
	Handling this is simple, first divide n by 5 and remove all single 5s,
	then divide by 25 to remove extra 5s and so on.

	Following is the summarized formula for counting trailing 0s.
		Trailing 0s in n! = Count of 5s in prime factors of n!
                  = floor(n/5) + floor(n/25) + floor(n/125) + ....
    :param n:
    :return:
    """

    # Initialize result
    count = 0

    # Keep dividing n by
    # powers of 5 and
    # update Count
    i = 5
    while (n / i) >= 1:
        count += int(n / i)
        i *= 5

    return int(count)



