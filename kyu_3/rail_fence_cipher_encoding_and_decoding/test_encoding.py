"""
Testing Encoding functionality
Created by Egor Kostan.

GitHub: https://github.com/ikostan
"""

# ALGORITHMS CIPHERS CRYPTOGRAPHY SECURITY STRINGS

import allure
import unittest
from utils.log_func import print_log
from kyu_3.rail_fence_cipher_encoding_and_decoding.encoding_and_decoding \
    import encode_rail_fence_cipher


@allure.epic('3 kyu')
@allure.parent_suite('Competent')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Rail Fence Cipher: Encoding and Decoding')
@allure.tag('ALGORITHMS',
            'CIPHERS',
            'CRYPTOGRAPHY',
            'SECURITY',
            'STRINGS')
@allure.link(
    url='https://www.codewars.com/kata/58c5577d61aefcf3ff000081/train/python',
    name='Source/Kata')
class EncodingTestCase(unittest.TestCase):
    """
    Testing Encoding functionality
    """

    def test_encoding(self):
        """
        Testing Encoding functionality
        """

        allure.dynamic.title("Testing Encoding functionality")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Verify cipher function. This \"encode\" is used to encode "
            "a string by placing each character successively in a "
            "diagonal along a set of \"rails\". </p>")

        test_data = (
            ("WEAREDISCOVEREDFLEEATONCE", 3, "WECRLTEERDSOEEFEAOCAIVDEN"),
            ("Hello, World!", 3, "Hoo!el,Wrdl l"),
            ("Hello, World!", 4, "H !e,Wdloollr"),
            ("", 3, ""),
            ('WEAREDISCOVEREDFLEEATONCE', 4, 'WIREEEDSEEEACAECVDLTNROFO'),
            ('WEAREDISCOVEREDFLEEATONCE', 6, 'WVTEOEAOACRENRSEECEIDLEDF'),
            ('WEAREDISCOVEREDFLEEATONCE', 10, 'WEEEAALTRFOEDNDECIRESECVO'),
            ("WEAREDISCOVEREDFLEEATONCE", 5, 'WCLEESOFECAIVDENRDEEAOERT'),
        )

        for string, n, expected in test_data:
            actual_result = encode_rail_fence_cipher(string, n)
            print_log(string=string,
                      n=n,
                      expected=expected,
                      actual_result=actual_result)

            with allure.step("Enter a test string and compare "
                             "the output vs expected result"):
                self.assertEqual(expected, actual_result)
