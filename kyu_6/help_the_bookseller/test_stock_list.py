#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS ALGORITHMS

import allure
import unittest
from utils.log_func import print_log
from kyu_6.help_the_bookseller.stock_list import stock_list


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("Algorithms")
@allure.story("Help the bookseller !")
@allure.tag('FUNDAMENTALS', 'ALGORITHMS')
@allure.link(url='https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python',
             name='Source/Kata')
class StockListTestCase(unittest.TestCase):
    """
    Testing stock_list function
    """

    def test_format_duration(self):
        allure.dynamic.title("Testing stock_list function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p>You will be given a stocklist (e.g. : L) and a list of "
                                        "categories in capital letters. Your task is to verify that "
                                        "the function finds all the books of L with codes belonging "
                                        "to each category of M and to sum their quantity according to "
                                        "each category.</p>")

        test_data = [
            (["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"],
             ["A", "B"],
             "(A : 200) - (B : 1140)"),
            (['BBAR 150', 'CDXE 515', 'BKWR 250', 'BTSQ 890', 'DRTY 600'],
             ['A', 'B', 'C', 'D'],
             '(A : 0) - (B : 1290) - (C : 515) - (D : 600)'),
            (['CBART 20', 'CDXEF 50', 'BKWRK 25', 'BTSQZ 89', 'DRTYM 60'],
             ['A', 'B', 'C', 'W'],
             '(A : 0) - (B : 114) - (C : 70) - (W : 0)'),
            (['ROXANNE 102', 'RHODODE 123', 'BKWRKAA 125', 'BTSQZFG 239', 'DRTYMKH 060'],
             ['B', 'R', 'D', 'X'],
             '(B : 364) - (R : 225) - (D : 60) - (X : 0)'),
            (['ROXANNE 102', 'RHODODE 123', 'BKWRKAA 125', 'BTSQZFG 239', 'DRTYMKH 060'],
             ['U', 'V', 'R'],
             '(U : 0) - (V : 0) - (R : 225)'),
            ([],
             ['B', 'R', 'D', 'X'],
             '')
        ]

        for listOfArt, listOfCat, expected in test_data:
            actual_result = stock_list(listOfArt, listOfCat)

            with allure.step("Enter test data ({}, {}) and verify the "
                             "expected output ({}) vs actual result ({})".format(listOfArt,
                                                                                 listOfCat,
                                                                                 expected,
                                                                                 actual_result)):
                print_log(listOfArt=listOfArt,
                          listOfCat=listOfCat,
                          expected=expected,
                          result=actual_result)

                self.assertEqual(expected,
                                 actual_result)
