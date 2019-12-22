def move_zeros(array: list):
    """
    An algorithm that takes an array and moves all of the
    zeros to the end, preserving the order of the other elements.
    :param array:
    :return:
    """

    moving_zero = True

    while moving_zero:
        moving_zero = False

        for i, a in enumerate(array):
            if a == 0 and array[i:].count(0) != len(array[i:]) and a is not False:
                del array[i]
                array.append(0)
                moving_zero = True
                break

    return array
