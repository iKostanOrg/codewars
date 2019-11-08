#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS PARSING STRINGS

import allure
import unittest
import pytest
from utils.log_func import print_log
from kyu_5.count_ip_addresses.ips_between import ips_between


@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Count IP Addresses')
@pytest.mark.skip(reason="The solution is not ready")
class IpsBetweenTestCase(unittest.TestCase):
	"""
	Testing ips_between function
	"""

	def test_ips_between(self):
		"""
		Testing ips_between function

		Testing a function that receives two IPv4 addresses,
		and returns the number of addresses between them
		(including the first one, excluding the last one).

		All inputs will be valid IPv4 addresses in the form
		of strings. The last address will always be greater
		than the first one.
		:return:
		"""

		data = [
			("10.0.0.0", "10.0.0.50", 50),
			("20.0.0.10", "20.0.1.0", 246),
			("10.0.0.0", "10.0.1.0", 256),
			("170.0.0.0", "170.1.0.0", 65536),
			("50.0.0.0", "50.1.1.1", 65793),
			("180.0.0.0", "181.0.0.0", 16777216),
			("1.2.3.4", "5.6.7.8", 67372036),
			("180.0.0.0", "181.0.0.0", 16777216),
			("117.170.96.190", "117.172.196.242", 156724)
		]

		for start, end, expected in data:

			print_log(start=start,
			          end=end,
			          expected=expected)

			self.assertEqual(expected,
			                 ips_between(start, end))
