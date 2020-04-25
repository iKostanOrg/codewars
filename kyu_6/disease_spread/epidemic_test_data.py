"""
Epidemic Test Data Class
"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


class EpidemicTestData:
    """
    Epidemic Test Data Class
    """

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
        return self.__tm

    @property
    def n(self):
        return self.__n

    @property
    def s0(self):
        return self.__s0

    @property
    def i0(self):
        return self.__i0

    @property
    def b(self):
        return self.__b

    @property
    def a(self):
        return self.__a

    @property
    def expected(self):
        return self.__expected

    def __repr__(self):
        return 'tm: {}, n: {}, s0: {}, i0: {}, b: {}, a: {}, expected: {}'.format(self.tm,
                                                                                  self.n,
                                                                                  self.s0,
                                                                                  self.i0,
                                                                                  self.b,
                                                                                  self.a,
                                                                                  self.expected)

    def __eq__(self, other):
        """
        Object comparison
        Override the default Equals behavior
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
