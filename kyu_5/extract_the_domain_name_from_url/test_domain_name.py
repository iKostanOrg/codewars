"""
Assert that 'domain_name' function
returns domain name from given URL string.
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS PARSING ALGORITHMS STRINGS REGULAR EXPRESSIONS
# DECLARATIVE PROGRAMMING ADVANCED LANGUAGE FEATURES

import unittest
import allure
from utils.log_func import print_log
from kyu_5.extract_the_domain_name_from_url.extract_domain_from_url \
    import domain_name


# pylint: disable-msg=R0801
@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Extract the domain name from a URL')
@allure.tag('FUNDAMENTALS',
            'PARSING',
            'ALGORITHMS',
            'STRINGS',
            'REGULAR EXPRESSIONS',
            'DECLARATIVE PROGRAMMING',
            'ADVANCED LANGUAGE FEATURES')
@allure.link(
    url='https://www.codewars.com/kata/514a024011ea4fb54200004b',
    name='Source/Kata')
# pylint: enable-msg=R0801
class DomainNameTestCase(unittest.TestCase):
    """
    Testing domain_name function
    """

    def test_domain_name(self):
        """
        Assert that 'domain_name' function
        returns domain name from given URL string.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing domain_name function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Assert that 'domain_name' function "
            "returns domain name from given URL string.</p>")
        # pylint: enable-msg=R0801
        test_data: tuple = (
            ("http://google.com", "google"),
            ("http://google.co.jp", "google"),
            ("www.xakep.ru", "xakep"),
            ("https://youtube.com", "youtube"))

        for url, expected in test_data:
            with allure.step("Enter test string and verify the output"):
                actual = domain_name(url)
                print_log(url=url,
                          expected=expected,
                          actual=actual)
                self.assertEqual(expected, actual)
