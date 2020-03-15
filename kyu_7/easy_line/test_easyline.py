#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import unittest
from utils.log_func import print_log
from kyu_7.easy_line.easyline import easy_line


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("Math")
@allure.story("Easy Line")
@allure.tag('FUNDAMENTALS', 'MATHEMATICS', 'ALGORITHMS', 'NUMBERS')
@allure.link(url='https://www.codewars.com/kata/'
                 '56e7d40129035aed6c000632/train/python',
             name='Source/Kata')
class EasyLineTestCase(unittest.TestCase):
    """
    We want to calculate the sum of the squares of the binomial
    coefficients on a given line with a function called easyline
    (or easyLine or easy-line).

    Can you write a program which calculate easyline(n) where n
    is the line number?

    The function will take n (with: n>= 0) as parameter and will
    return the sum of the squares of the binomial coefficients on line n.
    """

    def test_easy_line(self):
        allure.dynamic.title("Testing easy_line function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p>The function should take n (with: n>= 0) as parameter "
                                        "and must return the sum of the squares of the binomial "
                                        "coefficients on line n.</p>")

        test_data = (
            (0, 1),
            (1, 2),
            (4, 70),
            (7, 3432),
            (13, 10400600),
            (17, 2333606220),
            (19, 35345263800),
            (22, 2104098963720),
            (24, 32247603683100),
            (50, 100891344545564193334812497256)
        )

        for data in test_data:
            n: int = data[0]
            expected: int = data[1]
            actual: int = easy_line(n)

            with allure.step("Enter line number ({}) "
                             "and assert expected ({}) "
                             "vs actual ({}).".format(n, expected, actual)):
                print_log(n=n,
                          actual=actual,
                          expected=expected)

                self.assertEqual(expected, actual)
