"""
Test for -> Help the bookseller!.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS ALGORITHMS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_6.help_the_bookseller.stock_list import stock_list


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("Algorithms")
@allure.story("Help the bookseller !")
@allure.tag('FUNDAMENTALS',
            'ALGORITHMS')
@allure.link(
    url='https://www.codewars.com/kata/54dc6f5a224c26032800005c',
    name='Source/Kata')
class StockListTestCase(unittest.TestCase):
    """Testing stock_list function."""

    @parameterized.expand([
        (["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"],
         ["A", "B"], "(A : 200) - (B : 1140)"),
        (['BBAR 150', 'CDXE 515', 'BKWR 250', 'BTSQ 890', 'DRTY 600'],
         ['A', 'B', 'C', 'D'],
         '(A : 0) - (B : 1290) - (C : 515) - (D : 600)'),
        (['CBART 20', 'CDXEF 50', 'BKWRK 25', 'BTSQZ 89', 'DRTYM 60'],
         ['A', 'B', 'C', 'W'],
         '(A : 0) - (B : 114) - (C : 70) - (W : 0)'),
        (['ROXANNE 102', 'RHODODE 123', 'BKWRKAA 125', 'BTSQZFG 239',
          'DRTYMKH 060'], ['B', 'R', 'D', 'X'],
         '(B : 364) - (R : 225) - (D : 60) - (X : 0)'),
        (['ROXANNE 102', 'RHODODE 123', 'BKWRKAA 125', 'BTSQZFG 239',
          'DRTYMKH 060'],
         ['U', 'V', 'R'], '(U : 0) - (V : 0) - (R : 225)'),
        ([], ['B', 'R', 'D', 'X'], '')])
    def test_stock_list(self, list_of_art, list_of_cat, expected):
        """
        Testing stock_list function with various test data.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing stock_list function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>You will be given a stocklist (e.g. : L) and a list of "
            "categories in capital letters. Your task is to verify that "
            "the function finds all the books of L with codes belonging "
            "to each category of M and to sum their quantity according to "
            "each category.</p>")
        # pylint: enable-msg=R0801
        actual_result = stock_list(list_of_art, list_of_cat)
        with allure.step(f"Enter test data ({list_of_art}, "
                         f"{list_of_cat}) and verify the "
                         f"expected output ({expected}) vs "
                         f"actual result ({actual_result})"):
            print_log(list_of_artt=list_of_art,
                      list_of_cat=list_of_cat,
                      expected=expected,
                      result=actual_result)
            self.assertEqual(expected, actual_result)
