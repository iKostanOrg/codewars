"""
Test for -> Row of the odd triangle.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS PERFORMANCE

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_6.row_of_the_odd_triangle.odd_row import odd_row


# pylint: disable=R0801
@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Performance")
@allure.sub_suite("Unit Tests")
@allure.feature("Algorithms")
@allure.story("Row of the odd triangle")
@allure.tag('ALGORITHMS',
            'PERFORMANCE')
@allure.link(
    url='https://www.codewars.com/kata/5d5a7525207a674b71aa25b5',
    name='Source/Kata')
# pylint: enable=R0801
class OddRowTestCase(unittest.TestCase):
    """Testing odd_row function."""

    @parameterized.expand([
        (1, [1]),
        (2, [3, 5]),
        (13, [157, 159, 161, 163, 165, 167, 169, 171,
              173, 175, 177, 179, 181]),
        (19, [343, 345, 347, 349, 351, 353, 355, 357,
              359, 361, 363, 365, 367, 369, 371, 373,
              375, 377, 379]),
        (41, [1641, 1643, 1645, 1647, 1649, 1651, 1653,
              1655, 1657, 1659, 1661, 1663, 1665, 1667,
              1669, 1671, 1673, 1675, 1677, 1679, 1681,
              1683, 1685, 1687, 1689, 1691, 1693, 1695,
              1697, 1699, 1701, 1703, 1705, 1707, 1709,
              1711, 1713, 1715, 1717, 1719, 1721])])
    def test_odd_row(self, n, expected):
        """
        Testing odd_row function with various test data.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing odd_row function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Given a triangle of consecutive odd numbers find "
            "the triangle's row knowing its index (the rows are 1-indexed)</p>")
        # pylint: enable-msg=R0801
        actual_result = odd_row(n)
        with allure.step(f"Enter the triangle's row ({n}) "
                         f"and verify the expected output ({expected}) "
                         f"vs actual result ({actual_result})"):
            # pylint: disable=R0801
            print_log(n=n, expected=expected, result=actual_result)
            self.assertEqual(expected, actual_result)
            # pylint: disable=R0801
