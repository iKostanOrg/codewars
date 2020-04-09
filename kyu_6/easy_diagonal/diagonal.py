#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import math


def diagonal(n: int, p: int) -> int:
    """
    We want to calculate the sum of the binomial coefficients on a given diagonal.
    The sum on diagonal 0 is 8 (we'll write it S(7, 0), 7 is the number of the line
    where we start, 0 is the number of the diagonal).
    In the same way S(7, 1) is 28, S(7, 2) is 56.

    :param n: n is the line where we start and
    :param p: p is the number of the diagonal
    :return: the sum of the binomial coefficients on a given diagonal
    """
    if n < 0:
        raise ValueError('ERROR: invalid n ({}) value. n must be >= 0')

    if p < 0:
        raise ValueError('ERROR: invalid p ({}) value. p must be >= 0')

    #print('\nn: {}, p: {}'.format(n, p))
    #combinations = list()

    result = math.factorial(n + 1) // (math.factorial(p + 1) * math.factorial(n - p))

    #for row in range(p, n + 1):
        #temp = list()
        #for col in range(p, row + 1):
            #number = math.factorial(row) // (math.factorial(col) * math.factorial(row - col))
            #temp.append(number)
            #print('row: {}, col: {}, number: {} '.format(row, col, number), end='')
        #print(temp)
        #result += temp[0]
        #number = math.factorial(row) // (math.factorial(p) * math.factorial(row - p))
        #print(' ', number, end='')
        #result += number
        #combinations.append(temp)

    #print()
    #length: int = len('{}'.format(combinations[-1]))
    #for row in combinations:
        #space = ' ' * ((length - len('{}'.format(row))) // 2)
        #print('{}{}'.format(space, row))

    return result
