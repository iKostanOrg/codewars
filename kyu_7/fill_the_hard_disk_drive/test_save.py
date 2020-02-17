#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS LISTS DATA STRUCTURES ARRAYS

import allure
import unittest
from utils.log_func import print_log
from kyu_7.fill_the_hard_disk_drive.save import save


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Computer problem series #1: '
              'Fill the Hard Disk Drive')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class SaveTestCase(unittest.TestCase):
    """
    Testing 'save' function
    """

    def test_save_negative(self):
        """
        Testing 'save' function: negative

        The function should determine how many
        files of the copy queue you will be able
        to save into your Hard Disk Drive.
        :return:
        """

        allure.dynamic.title("Testing 'save' function: negative")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Enter sizes, hd and verify the output"):

            data = [
                ([11, 13, 15, 17, 19], 8, 0),
                ([45], 12, 0),
            ]

            for sizes, hd, expected in data:
                print_log(sizes=sizes,
                          hd=hd,
                          expected=expected)

                self.assertEqual(expected,
                                 save(sizes, hd))

    def test_save_positive(self):
        """
        Testing 'save' function: positive

        The function should determine how many
        files of the copy queue you will be able
        to save into your Hard Disk Drive.
        :return:
        """

        allure.dynamic.title("Testing 'save' function: positive")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Enter sizes, hd and verify the output"):

            data = [
                ([4, 4, 4, 3, 3], 12, 3),
                ([4, 4, 4, 3, 3], 11, 2),
                ([4, 8, 15, 16, 23, 42], 108, 6),
                ([13], 13, 1),
                ([1, 2, 3, 4], 250, 4),
                ([100], 500, 1),
            ]

            for sizes, hd, expected in data:

                print_log(sizes=sizes,
                          hd=hd,
                          expected=expected)

                self.assertEqual(expected,
                                 save(sizes, hd))
