"""
Solution for -> flatten().

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def flatten(*args) -> list:
    """
    Flatten function.

    The method takes in any number of arguments
    and flattens them into a single array. If any
    of the arguments passed in are an array then
    the individual objects within the array will
    be flattened so that they exist at the same
    level as the other arguments. Any nested arrays,
    no matter how deep, should be flattened into the
    single array result.
    :return:
    """
    result: list = []

    if args:
        unpack(args, result)
    return result


def unpack(data, collection: list):
    """
    Unpack helper method.

    Unpack data until its not list or a tuple.
    :param data:
    :param collection:
    :return:
    """
    if isinstance(data, (list, tuple)):
        for d in data:
            unpack(d, collection)
    else:
        collection.append(data)

