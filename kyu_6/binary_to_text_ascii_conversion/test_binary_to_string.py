"""
Test for -> Binary to Text (ASCII) Conversion.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS BINARY ASCII CHARACTER ENCODINGS FORMATS STRINGS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_6.binary_to_text_ascii_conversion.binary_to_string \
    import binary_to_string


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Character Encodings")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('Binary to Text (ASCII) Conversion')
@allure.tag('FUNDAMENTALS',
            'BINARY',
            'ASCII',
            'CHARACTER ENCODINGS',
            'FORMATS',
            'STRINGS')
@allure.link(
    url='https://www.codewars.com/kata/5583d268479559400d000064',
    name='Source/Kata')
class SequenceTestCase(unittest.TestCase):
    """Testing binary_to_string function."""

    @parameterized.expand([])
    def test_binary_to_string(self):
        """
        Testing binary_to_string function with various test data.

        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing binary_to_string function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Test a function that takes in a binary string and returns "
            "the equivalent decoded text (the text is ASCII encoded).</p>")
        # pylint: enable-msg=R0801
        test_data: tuple = (
            ('0100100001100101011011000110110001101111', 'Hello'),
            ('00110001001100000011000100110001', '1011'),
            ('010100110111000001100001011100100110101101'
             '110011001000000110011001101100011001010111'
             '011100101110001011100010000001100101011011'
             '010110111101110100011010010110111101101110'
             '011100110010000001110010011000010110111000'
             '100000011010000110100101100111011010000010'
             '0001', 'Sparks flew.. emotions ran high!'),
            ('001000010100000000100011001001000010010101'
             '011110001001100010101000101000001010010101'
             '000101010111010001010111001001110100011110'
             '010101010101001001010011110100110001100100'
             '011001100110011101100010011000100110100001'
             '101110011011010100100101001011010000100100'
             '101001001011010010000100100101010101010011'
             '110010100000111111001111100011111100111100'
             '011111100111111001111110011111100111111000'
             '101001001010000010101000100110001001010101'
             '111000111001001110000011011100110001001100'
             '110010111100101101001011110010101000101101'
             '0010101000101111',
             '!@#$%^&*()QWErtyUIOLdfgbbhnmIKBJKHIUO'
             '(?>?<~~~~~)(*&%^98713/-/*-*/'),
            ('011001100111011101101111001100010110001101'
             '101110001101100110011001101010011100010110'
             '010101110001', 'fwo1cn6fjqeq'))

        for binary, expected in test_data:
            actual_result = binary_to_string(binary)
            with allure.step(f"Enter a binary ({binary}) and verify the "
                             f"expected output ({expected}) vs "
                             f"actual result ({actual_result})"):

                print_log(binary=binary,
                          expected=expected,
                          result=actual_result)

                self.assertEqual(expected,
                                 actual_result)
