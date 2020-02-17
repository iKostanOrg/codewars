#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS REGULAR EXPRESSIONS DECLARATIVE PROGRAMMING ADVANCED LANGUAGE FEATURES STRINGS

import unittest
import allure
from utils.log_func import print_log
from kyu_7.password_validator.password import password


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Password validator')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class PasswordTestCase(unittest.TestCase):
    """
    Testing password function
    """

    def test_password(self):
        """
        Testing password function with various test inputs
        :return:
        """

        allure.dynamic.title("Testing password function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Enter test string and verify the result"):
            test_data = [
                ("Abcd1234", True),
                ("Abcd123", False),
                ("abcd1234", False),
                ("AbcdefGhijKlmnopQRsTuvwxyZ1234567890", True),
                ("ABCD1234", False),
                ("Ab1!@#$%^&*()-_+={}[]|\:;?/>.<,", True),
                ("!@#$%^&*()-_+={}[]|\:;?/>.<,", False),
                ("", False),
                (" aA1----", True),
                ("4aA1----", True),
            ]

            for string, expected in test_data:
                print_log(string=string, expected=expected)
                self.assertEqual(expected, password(string))
