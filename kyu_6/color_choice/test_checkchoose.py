#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS

import allure
import unittest
from utils.log_func import print_log
from kyu_6.color_choice.checkchoose import checkchoose


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("Factorial")
@allure.story('Color Choice')
@allure.tag('FUNDAMENTALS')
@allure.link(url='https://www.codewars.com/kata/55be10de92aad5ef28000023/train/python',
             name='Source/Kata')
class CheckchooseTestCase(unittest.TestCase):
    """
    Testing checkchoose function
    """

    def test_checkchoose(self):
        """
        In mathematics the number of x combinations you can take from a
        set of n elements is called the binomial coefficient of n and x,
        or more often n choose x. The formula to compute m = n choose x is:
        m = n! / (x! * (n - x)!) where ! is the factorial operator.

        You are a renowned poster designer and painter. You are asked to
        provide 6 posters all having the same design each in 2 colors.
        Posters must all have a different color combination and you have
        the choice of 4 colors: red, blue, yellow, green. How many colors
        can you choose for each poster?
        """
        allure.dynamic.title("Testing checkchoose function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p>Knowing m (number of posters to design), knowing n "
                                        "(total number of available colors), let us search x "
                                        "(number of colors for each poster so that each poster "
                                        "has a unique combination of colors and the number of "
                                        "combinations is exactly the same as the number of posters). "
                                        "In other words we must find x such as n choose x = m (1) "
                                        "for a given m and a given n; m >= 0 and n > 0. If many x "
                                        "are solutions give as result the smallest x. It can happen "
                                        "that when m is given at random there are no x satisfying "
                                        "equation (1) then return -1.</p>")


        test_data = (
            (6, 4, 2),
            (4, 4, 1),
            (4, 2, -1),
            (35, 7, 3),
            (36, 7, -1),
            (1, 6, 0),
            (1, 15, 0),
            (2, 12, -1),
            (75788358475481302186, 87, -1),
        )

        for d in test_data:
            m = d[0]
            n = d[1]
            expected = d[2]
            result = checkchoose(m, n)

            with allure.step("Pass m: {}, "
                             "n: {} and assert the "
                             "result: {} vs "
                             "expected: {}".format(m, n, result, expected)):

                print_log(m=m, n=n, result=result, expected=expected)
                self.assertEqual(expected, result)
