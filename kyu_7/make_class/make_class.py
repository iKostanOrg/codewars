"""
make_class function implementation for -> Make Class
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def make_class(*args):
    """
    make_class function implementation
    :param args:
    :return:
    """
    class Class:
        def __init__(self, *vals):
            for arg, val in zip(args, vals):
                setattr(self, arg, val)
    return Class
