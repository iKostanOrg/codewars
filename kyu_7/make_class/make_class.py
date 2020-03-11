#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def make_class(*args):
    class Class:
        def __init__(self, *vals):
            for arg, val in zip(args, vals):
                setattr(self, arg, val)
    return Class
