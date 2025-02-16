"""
Test for -> String subpattern recognition II.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS STRINGS REGULAR EXPRESSIONS
# DECLARATIVE PROGRAMMING ADVANCED LANGUAGE FEATURES

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_6.string_subpattern_recognition_2.has_subpattern import has_subpattern


# pylint: disable-msg=R0801
@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Advanced Language Features")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('String sub-pattern recognition II')
@allure.tag('FUNDAMENTALS',
            'STRINGS',
            'REGULAR EXPRESSIONS',
            'DECLARATIVE PROGRAMMING',
            'ADVANCED LANGUAGE FEATURES')
@allure.link(
    url='https://www.codewars.com/kata/5a4a391ad8e145cdee0000c4',
    name='Source/Kata')
# pylint: enable-msg=R0801
class HasSubpatternTestCase(unittest.TestCase):
    """Testing 'has_subpattern' function."""

    @parameterized.expand([
        ("a", False),
        ("aaaa", True),
        ("abcd", False),
        ("babababababababa", True),
        ("ababababa", False),
        ("123a123a123a", True),
        ("123A123a123a", False),
        ("12aa13a21233", True),
        ("12aa13a21233A", False),
        ("abcdabcaccd", False),
        ("w9TkPyHgTygqGTCBnL94FFa5q1uvyBzCOFdzFGl3439FCsk59yjq\
         A7nT9g3N94nTzFkCy31AkN2Hdd2Fmyn5VFGCBN5n931mkaw14bXw\
         Aywzw1TwyoAB2yLdydPGALFv51Bj0Vnnd1VayBTsun1TV31yPmbj\
         PNaq1kuXoVGkokjTTd2LFbOV7n2XTayLnbBsTFmsdHuVaykF0V23\
         w3slOymC1OF4akgo5yGLFsGF139oTG7GsuuvVPwTy3dm5oglTlF4\
         FlqkNyFVFGvm1VuljHggH74nFwCFLy0n0qALdy0o4yyw592BovN7\
         Bvy1AGwVngklvBGB204H2BTXjAykyXBFja5ov4jTkTGybBnATCvO\
         llwGClTmvw9os9TyH41vvjmkVXdTw3aysnTBPTvvgmA51wvkn1T7\
         1OyyGLPgV9LdmqyldTwbdu0TqTH377kOynv3Byd0vVlynTkAyyj1\
         1dqyv5FN1TsTyv5Gajgvd0Xn2dCjvFXq3lykg7soolyksllVGNkV\
         3VFLqwvnyBPH1T1NoBuzLnmlC5lO7FlHFwNVT1AuGT2zNsdVodnl\
         TdnnnwOdNTg5qH0PPXl5FljvOu0vyqBFXLTz9uvAzP5b1lTkHG5a\
         TqzzwCOkwl0dBVGjbkdFFy4TljFaTGBdAVGT1luFVnByHvn2XvAB\
         lAOGw77BjTg1k5yV17ddCmP14GvL2P5XBTkTw95v3ksv5kqkyuCy\
         X430BAy2AB5NlC5wXbOv4zgVl9GLb5wBzaNdT7vyzslPBkws5Nw2\
         w0nvN1V5dG4qzLX7dsV1ujGu0lzVbmPkVB59sVVoVFBHPyOuygO0\
         ClwmA2bGkHLVayBb5Cayl2m9w4TBgkGbTw0lHB2VG5NnFwyF17Gk\
         Tn5TdH7HVnlyvG51do9k35zO4aqmPBTwnXu5wdBvvTPdL715ln4o\
         jGVTTlgks119kuCV3Ta5vLa7nqmdolmjPG5wqGynXG2n1XTCbz10\
         BadOFvTbbgHOnywVG50wwNnzObkddNF5BGzobX", True)])
    def test_has_subpattern(self, string, expected):
        """
        Testing 'has_subpattern' function with various test data.

        Verify that 'has_subpattern' function to returns
        either true/True or false/False if a string can be
        seen as the repetition of a simpler/shorter subpattern or not.

        1. if a subpattern has been used, it will be repeated
        at least twice, meaning the subpattern has to be
        shorter than the original string;

        2. the strings you will be given might or might not
        be created repeating a given subpattern, then
        shuffling the result.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'has_subpattern' (part 2) function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: enable-msg=R0801
        with allure.step("Pass the string and verify the output"):
            # pylint: disable-msg=R0801
            print_log(string=string, expected=expected)
            self.assertEqual(expected, has_subpattern(string))
            # pylint: enable-msg=R0801
