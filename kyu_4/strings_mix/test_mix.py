"""
Test for -> Strings Mix.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS STRINGS

import unittest
import allure
from utils.log_func import print_log
from kyu_4.strings_mix.solution import mix


@allure.epic("4 kyu")
@allure.parent_suite('Competent')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story("Strings Mix")
@allure.tag('FUNDAMENTALS',
            'STRINGS')
@allure.link(
    url='https://www.codewars.com/kata/5629db57620258aa9d000014',
    name='Source/Kata')
class MixTestCase(unittest.TestCase):
    """Testing solution for Strings Mix problem."""

    def test_smix(self):
        """
        Testing 'mix' function.

        Given two strings s1 and s2, the 'mix' function
        should visualize how different the two strings are.
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'mix' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing pmix function</p>"
            "<p>Given two strings s1 and s2, the 'mix' function should "
            "visualize how different the two strings are. We will only "
            "take into account the lowercase letters (a to z). First let "
            "us count the frequency of each lowercase letters in s1 and s2.</p>")
        # pylint: enable-msg=R0801
        test_data: tuple = (
            ("Are they here",
             "yes, they are here",
             "2:eeeee/2:yy/=:hh/=:rr"),
            ("looping is fun but dangerous",
             "less dangerous than coding",
             "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"),
            (" In many languages",
             " there's a pair of functions",
             "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt"),
            ("Lords of the Fallen",
             "gamekult",
             "1:ee/1:ll/1:oo"),
            ("codewars",
             "codewars",
             "",),
            ("A generation must confront the looming ",
             "codewarrs",
             "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr"))

        for s1, s2, expected in test_data:
            actual_result = mix(s1, s2)
            print_log(s1=s1,
                      s2=s2,
                      expected=expected,
                      actual_result=actual_result)

            with allure.step("Enter s1 and s2 strings and assert "
                             "the output vs expected result"):
                self.assertEqual(expected, actual_result)
