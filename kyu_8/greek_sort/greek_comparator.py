"""
Solution for -> Greek Sort
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


# the tuple greek_alphabet is defined in the global namespace
GREEK_ALPHABET: tuple = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta',
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu',
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')


def greek_comparator(lhs: str, rhs: str) -> int:
    """
    A custom comparison function of two arguments (iterable elements)
    which should return a negative, zero or positive number depending
    on whether the first argument is considered smaller than, equal to,
    or larger than the second argument
    :param lhs: str
    :param rhs: str
    :return: int
    """
    return GREEK_ALPHABET.index(lhs) - GREEK_ALPHABET.index(rhs)
