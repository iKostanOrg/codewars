#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def sort_array(source_array: list) -> list:
    """
    Sorting ascending odd numbers but even
    numbers must be on their places.

    Zero isn't an odd number and you don't
    need to move it. If you have an empty array,
    ou need to return it.

    :param source_array:
    :return:
    """
    output: list = source_array[:]
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i_o, o in enumerate(output):
            if output[i_o] != 0 and output[i_o] % 2 != 0:
                for i_b, b in enumerate(output):
                    if output[i_b] != 0 and output[i_b] % 2 != 0 and output[i_o] > output[i_b] and i_o < i_b:
                        is_sorted = False
                        output[i_o], output[i_b] = b, o
                        break

    return output
