"""
Test for -> No arithmetic progressions
Testing sequence function
A function f(n), should returns the n-th member of sequence.
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS

import unittest
import allure
import pytest
from utils.log_func import print_log
from kyu_6.no_arithmetic_progressions.sequence import sequence


# pylint: disable-msg=R0801
@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Math")
@allure.story('No arithmetic progressions')
@allure.tag('ALGORITHMS')
@allure.link(
    url='https://www.codewars.com/kata/5e0607115654a900140b3ce3/train/python',
    name='Source/Kata')
# pylint: enable-msg=R0801
@pytest.mark.skip(reason="The solution is not ready")
class SequenceTestCase(unittest.TestCase):
    """
    Testing sequence function
    """

    def test_sequence(self):
        """
        A function f(n), should returns the n-th member of sequence.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing sequence function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Consider a sequence, which is formed by the following"
            " rule: next term is taken as the smallest possible "
            "non-negative integer, which is not yet in the sequence, "
            "so that no 3 terms of sequence form an arithmetic "
            "progression.</p>")
        # pylint: enable-msg=R0801
        test_data = (
            (1233, 62047),
            (0, 0),
            (1, 1),
            (2, 3),
            (3, 4),
            (4, 9),
            (6541, 717373),
            (7878, 790248),
            (1435, 67909),
            (6457, 715501))

        for n, expected in test_data:
            actual_result = sequence(n)
            # pylint: disable-msg=R0801
            with allure.step(
                    f"Enter a number ({n}) and verify the "
                    f"expected output ({expected}) vs "
                    f"actual result ({actual_result})"):
                print_log(n=n,
                          expected=expected,
                          result=actual_result)

                self.assertEqual(expected,
                                 actual_result)
            # pylint: enable-msg=R0801
