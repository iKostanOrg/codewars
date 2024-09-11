"""
Test for -> Unique In Order
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS ADVANCED LANGUAGE FEATURES ALGORITHMS

import unittest
import allure
from utils.log_func import print_log
from kyu_6.unique_in_order.unique_in_order import unique_in_order


# pylint: disable-msg=R0801
@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Advanced Language Features")
@allure.sub_suite("Unit Tests")
@allure.feature("Algorithms")
@allure.story('Unique In Order')
@allure.tag('FUNDAMENTALS',
            'ADVANCED LANGUAGE FEATURES',
            'ALGORITHMS')
@allure.link(
    url='https://www.codewars.com/kata/54e6533c92449cc251001667',
    name='Source/Kata')
# pylint: enable-msg=R0801
class UniqueInOrderTestCase(unittest.TestCase):
    """
    Testing the 'unique_in_order' function
    """

    def test_unique_in_order(self):
        """
        Testing the 'unique_in_order' function
        with various test data
        :return:
        """

        allure.dynamic.title("Testing the 'unique_in_order' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p></p>")
        # pylint: disable-msg=C0301
        with allure.step("Pass test data and verify the output"):
            data = [
                ('AAAABBBCCDAABBB',
                 ['A', 'B', 'C', 'D', 'A', 'B'],
                 'Should reduce duplicates'),
                ('ABBCcAD',
                 ['A', 'B', 'C', 'c', 'A', 'D'],
                 'Should be case-sensitive'),
                ([1, 2, 2, 3, 3],
                 [1, 2, 3],
                 'Should work with different element types'),
                ('ooooDDDDDdddddvOORRRRvvvFFFFpppppeeeeeppppIIIIssss'
                 'NUUUUjjVVVVVVVnnnZfffffjjjYYYYYkkkOOOOTvvvMMMtttttdyyyyFFFFCVVVVNNNuuuuufffQQQQQfffiiii',
                 ['o', 'D', 'd', 'v', 'O', 'R', 'v', 'F', 'p', 'e', 'p', 'I', 's', 'N', 'U', 'j', 'V', 'n', 'Z', 'f',
                  'j', 'Y', 'k', 'O', 'T', 'v', 'M', 't', 'd', 'y', 'F', 'C', 'V', 'N', 'u', 'f', 'Q', 'f', 'i'],
                 'Should work with randomly generated sequence'),
                ([-544706949, 1830150107, 1830150107, 1830150107, 1830150107, -1251355533, -1251355533, -1251355533,
                  -1251355533, -707089731, -707089731, -707089731, -707089731, 509047895, 509047895, 509047895,
                  509047895, -1478087323, -1478087323, -1478087323, -1478087323, -1478087323, -1228474529, -1228474529,
                  -1228474529, -27169356, -27169356, -1573356849, 1825933760, 1825933760, -101353285, -960509376,
                  -960509376, -960509376, 1631449194, 1631449194, 1631449194, 1631449194, -701582506, -701582506,
                  -1257392178, -1257392178, -909724592, -909724592, -909724592, -909724592, -909724592, -1610827611,
                  356483390, -721079729, -721079729, -721079729, -721079729, 327193119, 327193119, 327193119, 946667439,
                  1773522857, -94646693, -94646693, -94646693, 1202235680, -1682985580, -1682985580, -1682985580,
                  -1682985580, -1682985580, -308066619, 807682642, 1886853360, 1165912447, -1816272783, -1816272783,
                  -1816272783, -1816272783, 2088008817, -2119157678, -2119157678, -2119157678, -2119157678, 1041981535,
                  1041981535, 1041981535, 1041981535, 1041981535, 661938680, 661938680, 661938680, 661938680, 438934930,
                  1442648715, 1442648715, 468638621, 468638621, 468638621, 258893461, -46757153, -46757153, 1997749513,
                  1997749513, 1997749513, 1997749513, 78748495, 78748495, 78748495, 1555244045, 1506976994, 1506976994,
                  1506976994, -804276632, -804276632, -804276632, -804276632, -804276632, -367750677, -733550250,
                  -733550250, -733550250, -733550250],
                 [-544706949, 1830150107, -1251355533, -707089731, 509047895, -1478087323, -1228474529, -27169356,
                  -1573356849, 1825933760, -101353285, -960509376, 1631449194, -701582506, -1257392178, -909724592,
                  -1610827611, 356483390, -721079729, 327193119, 946667439, 1773522857, -94646693, 1202235680,
                  -1682985580, -308066619, 807682642, 1886853360, 1165912447, -1816272783, 2088008817, -2119157678,
                  1041981535, 661938680, 438934930, 1442648715, 468638621, 258893461, -46757153, 1997749513, 78748495,
                  1555244045, 1506976994, -804276632, -367750677, -733550250],
                 'Should work with randomly generated sequence')

            ]
            # pylint: enable-msg=C0301
            for test_data, expected, msg in data:
                print_log(iterable=test_data, expected=expected, msg=msg)
                self.assertEqual(expected, unique_in_order(test_data), msg=msg)
