#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import unittest
from utils.log_func import print_log
from kyu_6.easy_diagonal.diagonal import diagonal


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("Algorithms")
@allure.story('Easy Diagonal')
@allure.tag("FUNDAMENTALS", "ALGORITHMS")
@allure.link(url='https://www.codewars.com/kata/'
                 '559b8e46fa060b2c6a0000bf/train/python',
             name='Source/Kata')
class EasyDiagonalTestCase(unittest.TestCase):
    """
    Testing easy_diagonal function
    """
    def test_easy_diagonal(self):
        """
        Testing easy_diagonal function
        :param self:
        :return:
        """
        allure.dynamic.title("Testing easy_diagonal function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p>"
                                        "We want to calculate the sum of the binomial coefficients on a "
                                        "given diagonal. The sum on diagonal 0 is 8 (we'll write it S(7, 0), "
                                        "7 is the number of the line where we start, 0 is the number of the diagonal). "
                                        "In the same way S(7, 1) is 28, S(7, 2) is 56."
                                        "</p>")

        test_data = (
            (7, 0, 8),
            (7, 1, 28),
            (7, 2, 56),
            (20, 3, 5985),
            (100, 0, 101),
            (20, 4, 20349),
            (20, 15, 20349),
            (1291, 5, 6385476296235036),
            (129100, 5, 6429758786797926366807779220),
        )

        for td in test_data:
            n = td[0]
            p = td[1]
            expected = td[2]
            result = diagonal(n, p)
            print_log(n=n, p=p, expected=expected, result=result)
            with allure.step("Enter n: {}, "
                             "p: {} and assert the "
                             "expected: {} vs "
                             "result: {}".format(n, p, expected, result)):
                self.assertEqual(expected, result)
