"""
Test for -> Count IP Addresses
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS PARSING STRINGS

import unittest
import pytest
import allure
from utils.log_func import print_log
from kyu_5.count_ip_addresses.ips_between import ips_between


# pylint: disable-msg=R0801
@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Count IP Addresses')
@allure.tag('ALGORITHMS',
            'PARSING',
            'STRINGS')
@allure.link(url='https://www.codewars.com/kata/526989a41034285187000de4/train/python',
             name='Source/Kata')
@pytest.mark.skip(reason="The solution is not ready")
# pylint: enable-msg=R0801
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
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing alphabet_war function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing a function that receives two IPv4 addresses, "
            "and returns the number of addresses between them (including "
            "the first one, excluding the last one).</p>"
            "<p>All inputs will be valid IPv4 addresses in the form "
            "of strings. The last address will always be greater "
            "than the first one.</p>")
        # pylint: enable-msg=R0801
        test_data = [
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

        for start, end, expected in test_data:
            result = ips_between(start, end)

            with allure.step(f"Enter test data (start: {start}, "
                             f"end: {end}) and verify "
                             f"the output ({result}) "
                             f"vs expected ({expected})"):
                print_log(start=start,
                          end=end,
                          result=result,
                          expected=expected)

                self.assertEqual(expected,
                                 result)
