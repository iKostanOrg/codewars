#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


class EpidemicTestData:

	def __init__(self, tm, n, s0, i0, b, a, expected):
		self._tm = tm
		self._n = n
		self._s0 = s0
		self._i0 = i0
		self._b = b
		self._a = a
		self._expected = expected

	@property
	def tm(self):
		return self._tm

	@property
	def n(self):
		return self._n

	@property
	def s0(self):
		return self._s0

	@property
	def i0(self):
		return self._i0

	@property
	def b(self):
		return self._b

	@property
	def a(self):
		return self._a

	@property
	def expected(self):
		return self._expected

	def __repr__(self):
		return 'tm: {}, n: {}, s0: {}, i0: {}, b: {}, a: {}, expected: {}'.format(self.tm,
		                                                                         self.n,
		                                                                         self.s0,
		                                                                         self.i0,
		                                                                         self.b,
		                                                                         self.a,
		                                                                         self.expected)

	def __cmp__(self, other):
		"""
		Object comparison
		:param other:
		:return:
		"""
		return self.tm == other.tm and \
		       self.n == other.n and \
		       self.s0 == other.s0 and \
		       self.i0 == other.i0 and \
		       self.a == other.a and \
		       self.b == other.b and \
		       self.expected == other.expected
