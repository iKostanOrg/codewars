#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def monkey_count(n: int) -> list:
    """
    You take your son to the forest to see the monkeys.
    You know that there are a certain number there (n),
    but your son is too young to just appreciate the full
    number, he has to start counting them from 1.

    As a good parent, you will sit and count with him.
    Given the number (n), populate an array with all
    numbers up to and including that number, but
    excluding zero.
    :param n:
    :return:
    """

    monkeys = list()

    for n in range(1, n + 1):
        monkeys.append(n)

    return monkeys
