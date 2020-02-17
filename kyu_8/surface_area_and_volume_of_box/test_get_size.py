#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS GEOMETRY ALGEBRA MATHEMATICS ALGORITHMS

import unittest
import allure
from utils.log_func import print_log
from kyu_8.surface_area_and_volume_of_box.get_size import get_size


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Math")
@allure.sub_suite("Unit Tests")
@allure.feature("Geometry")
@allure.story('Surface Area and Volume of a Box')
@allure.tag('FUNDAMENTALS',
            'GEOMETRY',
            'ALGEBRA',
            'MATHEMATICS',
            'ALGORITHMS')
@allure.link(url='https://www.codewars.com/kata/565f5825379664a26b00007c/train/python',
             name='Source/Kata')
class GetSizeTestCase(unittest.TestCase):
    """
    Testing get_size function
    """

    def test_get_size(self):
        """
        Testing get_size function with various inputs
        :return:
        """

        allure.dynamic.title("get_size function tests")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Pass w, h, and d values and verify the result"):
            w, h, d = 4, 2, 6
            expected = [88, 48]

            print_log(w=w,
                      h=h,
                      d=d,
                      expected=expected)
            self.assertEqual(get_size(w, h, d), expected)

        with allure.step("Pass w, h, and d values and verify the result"):
            w, h, d = 1, 1, 1
            expected = [6, 1]

            print_log(w=w,
                      h=h,
                      d=d,
                      expected=expected)
            self.assertEqual(get_size(w, h, d), expected)

        with allure.step("Pass w, h, and d values and verify the result"):
            w, h, d = 1, 2, 1
            expected = [10, 2]

            print_log(w=w,
                      h=h,
                      d=d,
                      expected=expected)
            self.assertEqual(get_size(w, h, d), expected)

        with allure.step("Pass w, h, and d values and verify the result"):
            w, h, d = 1, 2, 2
            expected = [16, 4]

            print_log(w=w,
                      h=h,
                      d=d,
                      expected=expected)
            self.assertEqual(get_size(w, h, d), expected)

        with allure.step("Pass w, h, and d values and verify the result"):
            w, h, d = 10, 10, 10
            expected = [600, 1000]

            print_log(w=w,
                      h=h,
                      d=d,
                      expected=expected)
            self.assertEqual(get_size(w, h, d), expected)
