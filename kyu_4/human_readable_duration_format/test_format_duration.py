"""
Test for 'Human readable duration format'.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS FORMATS STRINGS DATES/TIME FORMATTING

import unittest
from parameterized import parameterized
import allure
from utils.log_func import print_log
from kyu_4.human_readable_duration_format.format_duration \
    import format_duration


# pylint: disable-msg=R0801
@allure.epic('4 kyu')
@allure.parent_suite('Competent')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Human readable duration format')
@allure.tag('ALGORITHMS',
            'FORMATS',
            'STRINGS',
            'DATES/TIME',
            'FORMATTING')
@allure.link(
    url='https://www.codewars.com/kata/52742f58faf5485cae000b9a',
    name='Source/Kata')
# pylint: enable-msg=R0801
class FormatDurationTestCase(unittest.TestCase):
    """Testing format_duration."""

    @parameterized.expand([
        (1, "1 second"),
        (62, "1 minute and 2 seconds"),
        (120, "2 minutes"),
        (3600, "1 hour"),
        (3662, "1 hour, 1 minute and 2 seconds"),
        (15731080,
         '182 days, 1 hour, 44 minutes and 40 seconds'),
        (132030240,
         '4 years, 68 days, 3 hours and 4 minutes'),
        (205851834,
         '6 years, 192 days, 13 hours, 3 minutes and 54 seconds'),
        (253374061,
         '8 years, 12 days, 13 hours, 41 minutes and 1 second'),
        (242062374,
         '7 years, 246 days, 15 hours, 32 minutes and 54 seconds'),
        (101956166,
         '3 years, 85 days, 1 hour, 9 minutes and 26 seconds'),
        (33243586,
         '1 year, 19 days, 18 hours, 19 minutes and 46 seconds'),
        (9041160,
         '104 days, 15 hours and 26 minutes')])
    def test_format_duration(self, seconds, expected):
        """
        Test format_duration function.

        Test a function which formats a duration,
        given as a number of seconds, in a human-friendly way.

        The function must accept a non-negative integer.
        If it is zero, it just returns "now". Otherwise,
        the duration is expressed as a combination of years,
        days, hours, minutes and seconds.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing format_duration")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Test a function which formats a duration, given as a "
            "number of seconds, in a human-friendly way.</p>"
            "<p>The function must accept a non-negative integer. "
            "If it is zero, it just returns \"now\". Otherwise, "
            "the duration is expressed as a combination of years, "
            "days, hours, minutes and seconds.</p>")
        # pylint: enable-msg=R0801
        actual_result = format_duration(seconds)
        with allure.step(f"Enter seconds ({seconds}) and verify the "
                         f"expected output ({expected}) vs "
                         f"actual result ({actual_result})"):
            print_log(seconds=seconds,
                      expected=expected,
                      result=actual_result)
            self.assertEqual(expected, actual_result)
