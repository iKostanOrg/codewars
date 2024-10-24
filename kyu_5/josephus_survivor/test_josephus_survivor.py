"""
Test for -> Josephus Survivor
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS MATHEMATICS NUMBERS LISTS DATA STRUCTURES ARRAYS

import unittest
import pytest
import allure
from utils.log_func import print_log
from kyu_5.josephus_survivor.josephus_survivor \
    import josephus_survivor


@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite('Algorithms')
@allure.sub_suite("Unit Tests")
@allure.feature('Math')
@allure.story('Josephus Survivor')
@allure.tag('ALGORITHMS',
            'MATHEMATICS',
            'NUMBERS',
            'LISTS',
            'DATA STRUCTURES',
            'ARRAYS')
@allure.link(
    url='https://www.codewars.com/kata/555624b601231dc7a400017a',
    name='Source/Kata')
@pytest.mark.skip(reason="The solution is not ready")
class JosephusSurvivorTestCase(unittest.TestCase):
    """
    Testing josephus_survivor function
    """

    def test_josephus_survivor(self):
        """
        In this kata you have to correctly return who
        is the "survivor", ie: the last element of a
        Josephus permutation.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing josephus_survivor function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>In this kata you have to verify that the function "
            "correctly returns who is the \"survivor\", ie: the "
            "last element of a Josephus permutation.</p>")
        # pylint: enable-msg=R0801
        test_data: tuple = (
            ((7, 3), 4),
            ((11, 19), 10),
            ((1, 300), 1),
            ((14, 2), 13),
            ((100, 1), 100))

        for test_data, expected in test_data:
            total = test_data[0]
            eliminated = test_data[1]
            result = josephus_survivor(total, eliminated)

            with allure.step(f"Enter test data "
                             f"(n: {total}, k: {eliminated}) and verify "
                             f"the output ({result}) "
                             f"vs expected ({expected})"):

                print_log(total=total,
                          eliminated=eliminated,
                          result=result,
                          expected=expected)

                self.assertEqual(expected,
                                 result)
