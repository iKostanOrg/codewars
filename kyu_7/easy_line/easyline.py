#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def easy_line(n: int) -> int:
    """
    The function will take n (with: n>= 0) as parameter
    and will return the sum of the squares of the binomial
    coefficients on line n.
    :param n:
    :return:
    """
    coefficient: int = 1
    total: int = 0

    for i in range(n + 1):
        total += coefficient ** 2
        coefficient = coefficient * (n - i) // (i + 1)
        
    return total
