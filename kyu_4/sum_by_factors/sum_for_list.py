#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from utils.primes.primes_generator import gen_primes


def sum_for_list(lst: list) -> list:
    """
    Given an array of positive or negative integers I= [i1,..,in]
    the function have to produce a sorted array P of the form:

    [ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

    P will be sorted by increasing order of the prime numbers.

    :param lst: an array of positive or negative integers
    :return: sorted array P
    """
    max_l = max(lst) if abs(max(lst)) > abs(min(lst)) else abs(min(lst))
    results = list()

    for prime in gen_primes():
        # stop execution in case current
        # prime is greater than max digit
        if prime > max_l:
            break

        temp = list()  # holds temporary results
        sum_digits = 0  # holds sum of all ij of I for which p is a prime factor

        for digit in lst:
            # negative m for all negative digits
            # and vice versa
            m = 1
            if digit < 0:
                m = -1

            if digit % (prime * m) == 0:
                if len(temp) == 0:
                    temp.append(prime)
                sum_digits += digit

        # add result in case prime in temp list
        if len(temp) > 0:
            temp.append(sum_digits)
            results.append(temp)

    return results
