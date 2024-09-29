"""
Testing Decoding functionality

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS CIPHERS CRYPTOGRAPHY SECURITY STRINGS

import unittest
import allure
from utils.log_func import print_log
from kyu_3.rail_fence_cipher_encoding_and_decoding.encoding_and_decoding \
    import decode_rail_fence_cipher


# pylint: disable-msg=R0801
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
    url='https://www.codewars.com/kata/58c5577d61aefcf3ff000081',
    name='Source/Kata')
# pylint: enable-msg=R0801
class DecodingTestCase(unittest.TestCase):
    """
    Testing Decoding functionality
    """

    def test_decoding(self):
        """
        Testing Decoding functionality
        """
        allure.dynamic.title("Testing Decoding functionality")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Verify cipher function. This \"decode\" is used "
            "to decode a string.</p>")

        test_data: tuple = (
            ("H !e,Wdloollr", 4, "Hello, World!"),
            ("WECRLTEERDSOEEFEAOCAIVDEN", 3, "WEAREDISCOVEREDFLEEATONCE"),
            ("", 3, ""),
            ("WEAREDISCOVEREDFLEEATONCE", 10, "WADCEDETNECOEFROIREESVELA"),
            ("WEAREDISCOVEREDFLEEATONCE", 9, "WADCEDETCOEFROIREESVELANE")
        )
        # pylint: disable-msg=R0801
        for string, n, expected in test_data:
            actual_result = decode_rail_fence_cipher(string, n)
            print_log(string=string,
                      n=n,
                      expected=expected,
                      actual_result=actual_result)

            with allure.step("Enter a test string and compare "
                             "the output vs expected result"):
                self.assertEqual(expected, actual_result)
        # pylint: enable-msg=R0801
