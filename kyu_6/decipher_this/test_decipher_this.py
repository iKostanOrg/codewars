"""
Test for -> Decipher this!
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS STRINGS ARRAYS CIPHERS
# ALGORITHMS CRYPTOGRAPHY SECURITY

import unittest
import allure
from kyu_6.decipher_this.solution import decipher_this
from utils.log_func import print_log


# pylint: disable-msg=R0801
@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("Algorithms")
@allure.story('Decipher this!')
@allure.tag('FUNDAMENTALS',
            'STRINGS',
            'ARRAYS',
            'CIPHERS',
            'ALGORITHMS',
            'CRYPTOGRAPHY',
            'SECURITY')
@allure.link(
    url='https://www.codewars.com/kata/581e014b55f2c52bb00000f8/train/python',
    name='Source/Kata')
# pylint: enable-msg=R0801
class DecipherThisTestCase(unittest.TestCase):
    """
    Testing decipher_this function
    """

    def test_decipher_this(self):
        """
        Testing decipher_this function
        :param self:
        :return:
        """
        allure.dynamic.title("Testing decipher_this function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>"
            "Given a secret message that you need to decipher.<br>"
            "<br>For each word:<br>"
            " * the second and the last letter is switched (e.g. "
            "Hello becomes Holle)<br> * the first letter is replaced "
            "by its character code (e.g. H becomes 72)<br>"
            "<br>Note: there are no special characters used, only "
            "letters and spaces."
            "</p>")

        test_data = (
            ("",
             ""),
            ('72olle 103doo 100ya',
             'Hello good day'),
            ('82yade 115te 103o',
             'Ready set go'),
            ("65 119esi 111dl 111lw 108dvei 105n 97n 111ka",
             "A wise old owl lived in an oak"),
            ("84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp",
             "The more he saw the less he spoke"),
            ("84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare",
             "The less he spoke the more he heard"),
            ("87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri",
             "Why can we not all be like that wise old bird"),
            ("84kanh 121uo 80roti 102ro 97ll 121ruo 104ple",
             "Thank you Piotr for all your help")
        )

        for text, expected in test_data:
            result = decipher_this(text)
            print_log(text=text,
                      expected=expected,
                      result=result)

            with allure.step("Enter test string and verify the output"):
                self.assertEqual(expected,
                                 result)
