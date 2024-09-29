"""
Test for -> Disease Spread
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS

import unittest
import allure
from utils.log_func import print_log
from kyu_6.disease_spread.epidemic import epidemic
from kyu_6.disease_spread.epidemic_test_data import EpidemicTestData


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite('Fundamentals')
@allure.sub_suite("Unit Tests")
@allure.feature('Math')
@allure.story('Disease Spread')
@allure.tag('FUNDAMENTALS')
@allure.link(
    url='https://www.codewars.com/kata/566543703c72200f0b0000c9/train/python',
    name='Source/Kata')
class EpidemicTestCase(unittest.TestCase):
    """
    Testing for solution Disease Spread
    """
    def test_epidemic(self):
        """
        Testing epidemic function
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing epidemic function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>The function epidemic should return the maximum number "
            "of infected as an integer (truncate to integer the result "
            "of max(I)).</p>")
        # pylint: enable-msg=R0801
        # tm , n, s0, i0, b, a, expected
        test_data = (
            EpidemicTestData(tm=18, n=432, s0=1004, i0=1,
                             b=0.00209, a=0.51, expected=420),
            EpidemicTestData(tm=12, n=288, s0=1007, i0=2,
                             b=0.00206, a=0.45, expected=461),
            EpidemicTestData(tm=13, n=312, s0=999, i0=1,
                             b=0.00221, a=0.55, expected=409),
            EpidemicTestData(tm=24, n=576, s0=1005, i0=1,
                             b=0.00216, a=0.45, expected=474),
            EpidemicTestData(tm=24, n=576, s0=982, i0=1,
                             b=0.00214, a=0.44, expected=460),
            EpidemicTestData(tm=20, n=480, s0=1000, i0=1,
                             b=0.00199, a=0.53, expected=386),
            EpidemicTestData(tm=28, n=672, s0=980, i0=1,
                             b=0.00198, a=0.44, expected=433),
            EpidemicTestData(tm=14, n=336, s0=996, i0=2,
                             b=0.00206, a=0.41, expected=483),
            EpidemicTestData(tm=13, n=312, s0=993, i0=2,
                             b=0.0021, a=0.51, expected=414),
            EpidemicTestData(tm=28, n=672, s0=999, i0=1,
                             b=0.00197, a=0.55, expected=368)
        )

        for etd in test_data:
            tm = etd.tm
            n = etd.n
            s0 = etd.s0
            i0 = etd.i0
            b = etd.b
            a = etd.a
            expected = etd.expected
            actual_result = epidemic(tm=tm, n=n, s0=s0, i0=i0, b=b, a=a)

            with allure.step(f"Enter test data ({etd}) and verify the "
                             f"expected output ({expected}) vs "
                             f"actual result ({actual_result})"):

                print_log(etd=etd,
                          expected=expected,
                          result=actual_result)

                self.assertEqual(expected,
                                 actual_result)
