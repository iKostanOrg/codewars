#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS MATHEMATICS NUMBERS LISTS DATA STRUCTURES ARRAYS

import unittest
import allure
import pytest

from utils.log_func import print_log
from kyu_5.josephus_survivor.josephus_survivor import josephus_survivor


@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite('Algorithms')
@allure.sub_suite("Unit Tests")
@allure.feature('Math')
@allure.story('Josephus Survivor')
@allure.tag('ALGORITHMS', 'MATHEMATICS', 'NUMBERS',
            'LISTS', 'DATA STRUCTURES', 'ARRAYS')
@allure.link(url='https://www.codewars.com/kata/555624b601231dc7a400017a/train/python',
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

        allure.dynamic.title("Testing josephus_survivor function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p>In this kata you have to verify that the function "
                                        "correctly returns who is the \"survivor\", ie: the "
                                        "last element of a Josephus permutation.</p>")

        test_data = [
            ((7, 3), 4),
            ((11, 19), 10),
            ((1, 300), 1),
            ((14, 2), 13),
            ((100, 1), 100)
        ]

        for test_data, expected in test_data:
            n = test_data[0]
            k = test_data[1]
            result = josephus_survivor(n, k)

            with allure.step("Enter test data (n: {}, k: {}) and verify "
                             "the output ({}) vs expected ({})".format(n,
                                                                       k,
                                                                       result,
                                                                       expected)):
                print_log(n=n,
                          k=k,
                          result=result,
                          expected=expected)

                self.assertEqual(expected,
                                 result)
