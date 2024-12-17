"""
Epidemic Test Data Class.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


class EpidemicTestData:
    """Epidemic Test Data Class."""

    def __init__(self, **kwargs):
        # tm, n, s0, i0, b, a, expected
        self.__tm = kwargs['tm']
        self.__n = kwargs['n']
        self.__s0 = kwargs['s0']
        self.__i0 = kwargs['i0']
        self.__b = kwargs['b']
        self.__a = kwargs['a']
        self.__expected = kwargs['expected']

    @property
    def tm(self):
        """
        Returns tm value.

        :return:
        """
        return self.__tm

    @property
    def n(self):
        """
        Returns n value.

        :return:
        """
        return self.__n

    @property
    def s0(self):
        """
        Returns s0 value.

        :return:
        """
        return self.__s0

    @property
    def i0(self):
        """
        Returns i0 value.

        :return:
        """
        return self.__i0

    @property
    def b(self):
        """
        Returns b value.

        :return:
        """
        return self.__b

    @property
    def a(self):
        """
        Returns a value.

        :return:
        """
        return self.__a

    @property
    def expected(self):
        """
        Returns expected value.

        :return:
        """
        return self.__expected

    def __repr__(self):
        """
        Repr function.

        :return:
        """
        return (f'tm: {self.tm}, n: {self.n}, s0: {self.s0}, '
                f'i0: {self.i0}, b: {self.b}, a: {self.a}, '
                f'expected: {self.expected}')

    def __eq__(self, other):
        """
        Object comparison.

        Override the default Equals behavior.
        :param other:
        :return:
        """
        return self.__class__ == other.__class__ and \
            self.tm == other.tm and \
            self.n == other.n and \
            self.s0 == other.s0 and \
            self.i0 == other.i0 and \
            self.a == other.a and \
            self.b == other.b and \
            self.expected == other.expected
