"""
Solution for -> Encrypt this!
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS STRINGS REGULAR EXPRESSIONS DECLARATIVE PROGRAMMING
# ADVANCED LANGUAGE FEATURES ARRAYS CIPHERS ALGORITHMS CRYPTOGRAPHY SECURITY

import unittest
import allure
from utils.log_func import print_log
from kyu_6.encrypt_this.solution import encrypt_this


# pylint: disable-msg=R0801
@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("Algorithms")
@allure.story('Encrypt this!')
@allure.tag('FUNDAMENTALS',
            'STRINGS',
            'REGULAR EXPRESSIONS',
            'DECLARATIVE PROGRAMMING',
            'ADVANCED LANGUAGE FEATURES',
            'ARRAYS',
            'CIPHERS',
            'ALGORITHMS',
            'CRYPTOGRAPHY',
            'SECURITY')
@allure.link(
    url='https://www.codewars.com/kata/5848565e273af816fb000449/train/python',
    name='Source/Kata')
# pylint: enable-msg=R0801
class EncryptThisTestCase(unittest.TestCase):
    """
    Testing encrypt_this function
    """

    def test_encrypt_this(self):
        """
        Testing encrypt_this function
        :param self:
        :return:
        """
        allure.dynamic.title("Testing encrypt_this function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>"
            "Your message is a string containing space separated words.<br>"
            "You need to encrypt each word in the message using the following"
            " rules:<br>"
            " * The first letter needs to be converted to its ASCII code.<br>"
            " * The second letter needs to be switched with the last letter<br>"
            "Keepin' it simple: There are no special characters in input."
            "</p>")

        test_data = (
            ("",
             ""),
            ("Hello",
             "72olle"),
            ("good",
             "103doo"),
            ("hello world",
             "104olle 119drlo"),
            ("A wise old owl lived in an oak",
             "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"),
            ("The more he saw the less he spoke",
             "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"),
            ("The less he spoke the more he heard",
             "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"),
            ("Why can we not all be like that wise old bird",
             "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"),
            ("Thank you Piotr for all your help",
             "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple")
        )

        for text, expected in test_data:
            result = encrypt_this(text)
            print_log(text=text, expected=expected, result=result)
            with allure.step("Enter test string and verify the output"):
                self.assertEqual(expected, result)
