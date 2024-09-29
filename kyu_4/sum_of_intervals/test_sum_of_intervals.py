"""
Test for -> Sum of Intervals

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS AGGREGATIONS ARITHMETIC MATHEMATICS NUMBERS INTEGERS

import unittest
import allure
from utils.log_func import print_log
from kyu_4.sum_of_intervals.sum_of_intervals import sum_of_intervals


@allure.epic('4 kyu')
@allure.parent_suite('Competent')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Aggregations")
@allure.story('Sum of Intervals')
@allure.tag('ALGORITHMS',
            'AGGREGATIONS',
            'ARITHMETIC',
            'MATHEMATICS',
            'NUMBERS',
            'INTEGERS')
@allure.link(url='https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python',
             name='Source/Kata')
class SumOfIntervalsTestCase(unittest.TestCase):
    """
    Testing sum_of_intervals function
    """

    def test_sum_of_intervals(self):
        """
        Testing sum_of_intervals function

        The function should accept an array of intervals,
        and return the sum of all the interval lengths.

        Overlapping intervals should only be counted once.

        Intervals
        Intervals are represented by a pair of integers in
        the form of an array. The first value of the interval
        will always be less than the second value.
        Interval example: [1, 5] is an interval from 1 to 5.
        The length of this interval is 4.
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing sum_of_intervals function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Testing sum_of_intervals function"
            "<p>The function should accept an array of intervals, "
            "and return the sum of all the interval lengths."
            "<p>Overlapping intervals should only be counted once."
            "<p>Intervals</p>"
            "<p>Intervals are represented by a pair of integers in"
            " the form of an array. The first value of the interval"
            " will always be less than the second value."
            " Interval example: [1, 5] is an interval from 1 to 5."
            " The length of this interval is 4.</p>")
        # pylint: enable-msg=R0801
        test_data = [
            ([(1, 5)], 4),
            ([(1, 5), (6, 10)], 8),
            ([(1, 5), (1, 5)], 4),
            ([(1, 4), (7, 10), (3, 5)], 7),
            ([(167, 273), (123, 340), (-15, 69), (-97, 319),
              (476, 493), (252, 428), (-263, -59), (258, 300),
              (-41, 52), (-417, -250), (-484, -81), (191, 195),
              (-232, 147)], 929),
            ([(282, 428), (-467, -405), (-473, 229), (143, 233), (217, 471),
              (-86, 179), (-49, 201), (-144, 420), (449, 476), (-211, -15),
              (-287, -173), (-212, 314), (-57, 322), (-34, 26), (106, 350),
              (-368, 427), (61, 300)], 949),
            ([(-45, 178), (108, 123), (83, 358), (2, 77), (363, 493), (356, 421),
              (-44, 304), (-419, -138), (-161, 159), (-237, 95), (341, 367),
              (145, 453), (442, 450), (156, 500)], 919),
            ([(-85, 47), (-153, 122), (-111, 312), (411, 469), (459, 464),
              (360, 428), (-149, 115)], 574),
            ([(289, 353), (342, 351), (-231, 202), (-304, -194), (31, 277), (-73, 247),
              (-371, -262), (77, 436), (368, 420), (235, 295), (-135, 294), (204, 325),
              (14, 344), (456, 494), (-500, 288), (326, 360), (313, 379), (-260, -94),
              (93, 328), (456, 493)], 974)
        ]

        for intervals, expected in test_data:
            actual_result = sum_of_intervals(intervals)
            print_log(intervals=intervals,
                      expected=expected,
                      actual_result=actual_result)

            with allure.step(f"Enter a list of intervals ({intervals}), "
                             f"calculate the result ({actual_result}) and "
                             f"compare vs expected ({expected})"):
                self.assertEqual(expected,
                                 actual_result)
