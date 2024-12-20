"""
make_class function implementation for -> Make Class.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def make_class(*args):
    """
    'make_class' function implementation.

    :param args:
    :return:
    """

    # pylint: disable-msg=R0903
    class Class:
        """Generic class."""

        def __init__(self, *vals):
            """
            Create a new Class instance.

            :param vals:
            """
            for arg, val in zip(args, vals):
                setattr(self, arg, val)
    # pylint: enable-msg=R0903
    return Class
