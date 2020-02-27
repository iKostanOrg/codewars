#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def thirt(n: int) -> int:
    """
    The function which processes this sequence of operations
    on an integer n (>=0). `thirt` will return the stationary number.
    :param n:
    :return:
    """
    remainders = (1, 10, 9, 12, 3, 4)

    while True:
        i = 0
        temp = 0
        t = str(n)[::-1]
        for s in t:
            temp += int(s) * remainders[i]
            if i + 1 < len(remainders):
                i += 1
            else:
                i = 0

        if int(n) == temp:
            return temp
        else:
            n = temp

