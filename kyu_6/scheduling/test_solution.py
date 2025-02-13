"""
Test for -> Scheduling (Shortest Job First or SJF).

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# SCHEDULING QUEUES ALGORITHMS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_6.scheduling.solution import shortest_job_first


# pylint: disable-msg=R0801
@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("Algorithms")
@allure.story('Scheduling (Shortest Job First or SJF)')
@allure.tag('SCHEDULING', 'QUEUES', 'ALGORITHMS')
@allure.link(
    url='https://www.codewars.com/kata/550cc572b9e7b563be00054f',
    name='Source/Kata')
# pylint: enable-msg=R0801
class SJFTestCase(unittest.TestCase):
    """Testing 'shortest_job_first' function."""

    # pylint: disable-msg=R0801
    @parameterized.expand([
        (([100], 0), 100),
        (([3, 10, 20, 1, 2], 0), 6),
        (([3, 10, 20, 1, 2], 1), 16),
        (([3, 10, 10, 20, 1, 2], 1), 16),
        (([3, 10, 10, 20, 1, 2], 2), 26),
        (([20, 20, 7, 15, 14, 10, 16, 16, 3, 18, 3, 1, 13, 1, 17, 2, 17, 17, 20,
           3, 12, 11, 9, 5, 11, 19, 15, 15, 1, 2, 19, 9, 20, 7, 11, 5, 4, 3, 5,
           8, 13, 8, 11, 3, 12, 20, 20, 10, 19, 20, 16, 5, 5, 9, 15, 1, 14, 10,
           13, 8, 11, 1, 20, 18, 9, 10, 3, 8, 11, 11, 17, 6, 7, 6, 12, 17, 8, 19,
           10, 5, 7, 8, 7, 11, 15, 12, 7, 6, 2, 14, 14, 2, 16, 3, 16, 6, 7, 15,
           20, 13, 2, 19, 5, 3, 4, 15, 10, 9, 10, 16, 10, 14, 4, 13, 4, 6, 1, 18,
           6, 10, 16, 4, 6, 6, 2, 8, 16, 18, 2, 15, 18, 15, 2], 75), 1008),
        (([4, 13, 13, 12, 17, 4, 15, 4, 12, 2, 15, 7, 2, 12, 19, 11, 10, 7, 11,
           18, 5, 7, 15, 20, 9, 16, 12, 17, 7, 2, 10, 19, 6, 9, 7, 16, 19, 16,
           15, 6, 17, 3, 13, 11, 19, 18, 13, 10, 5, 20, 5, 10, 9, 18, 14, 18, 8,
           15, 17, 10, 17, 5, 3, 1, 18, 5, 1, 19, 14, 4, 6, 19, 19, 3, 5, 3, 2, 4,
           9, 18, 1, 3, 11, 16, 8, 1, 6, 6, 10, 2, 17, 1, 16, 3, 3, 2, 16, 4, 13,
           20, 5, 20, 20, 5, 1, 20, 14, 4, 11, 5, 9, 2, 6, 20, 11, 17, 4, 12, 13,
           16, 13, 19, 5, 18, 20, 6, 19, 10, 19, 12, 4, 18, 5, 14, 9, 1, 1, 5, 13,
           14, 9, 18, 9, 11, 19, 10, 20, 17, 13, 1, 13, 8, 12, 2, 19, 3, 14, 1, 20,
           7, 14, 12, 11, 18, 3, 4, 9, 5, 19], 24), 275)])
    def test_sjf(self, n, expected):
        """
        Testing 'shortest_job_first' function with various test data.

        :return:
        """
        allure.dynamic.title("Testing 'shortest_job_first(' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Test a function that processes sequence of jobs "
            "and returns a positive integer representing the cc it"
            "takes to complete the job at index.</p>")
        # pylint: enable-msg=R0801
        jobs, index = n
        actual_result = shortest_job_first(jobs, index)
        # pylint: disable-msg=R0801
        with allure.step(f"Enter a n ({n}) and verify the "
                         f"expected output ({expected}) vs "
                         f"actual result ({actual_result})"):
            print_log(n=n, expected=expected, result=actual_result)
            self.assertEqual(expected, actual_result)
        # pylint: enable-msg=R0801
