#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

from utils.primes.primes_generator import gen_primes


def assert_sudoku_by_region(board: list) -> bool:
    """
    Assert Sudoku by region

    :param board: Sudoku list
    :return: boolean value (is Sudoku done or not)
    """
    row_length = len(board[0])

    step = 0
    for i in gen_primes():
        if row_length % i == 0:
            step = i
            break

    t, start, end = 0, 0, step

    while t < step:
        for i in range(0, row_length, step):
            region = list()
            for a in range(i, i + step):
                row = board[a][start: end]
                for b in row:
                    region.append(b)
            s_region = set(region)
            if len(s_region) != row_length:
                return False

        start, end = end, end + step
        t += 1

    return True
