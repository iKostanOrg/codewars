"""
Test for -> # Conversion between Kilobyte and KibiByte.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# MATHEMATICS STRINGS FUNDAMENTALS

import unittest
import allure
from parameterized import parameterized
from utils.log_func import print_log
from kyu_6.conversion_between_kilobyte_and_kibibyte.solution import (
    memorysize_conversion,
    unit_extractor)


# pylint: disable-msg=R0801
@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature("Math")
@allure.story('# Conversion between Kilobyte and KibiByte.')
@allure.tag('MATHEMATICS',
            'MATH',
            'STRINGS',
            'FUNDAMENTALS')
@allure.link(
    url='https://www.codewars.com/kata/5a115ff080171f9651000046',
    name='Source/Kata')
# pylint: enable-msg=R0801
class MemorySizeConversionTestCase(unittest.TestCase):
    """Test 'Conversion between Kilobyte and KibiByte' solution."""

    @parameterized.expand([
        ('1 KiB', '1.024 kB', '1 KiB is 1.024 kB'),
        ("1 MiB", "1.049 MB", "1 MiB is 1.049 MB"),
        ("1 GB", "0.931 GiB", "1 GB is 0.931 GiB"),
        ("163.287 GiB", "175.328 GB", "163.287 GiB GiB should equal 175.328 GB"),
        ('974.834 KiB', '998.23 kB', 'No trailing zeros allowed.')
    ])
    def test_memorysize_conversion(self, memory_size, expected, err):
        """
        Test 'memorysize_conversion' function with various test data.

        :param memory_size: str
        :param expected: str
        :param err: str
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'memorysize_conversion' function:")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>"
            "Your task is to write a conversion function between the kB and "
            "the KiB-Units. The function receives as parameter a memory size "
            "including a unit and converts into the corresponding unit of the "
            "other system:"
            "<ul>"
            "<li>10 KiB -> 10.24 kB</li>"
            "<li>1 kB -> 0.977 KiB</li>"
            "<li>10 TB -> 9.095 TiB</li>"
            "<li>4.1 GiB -> 4.402 GB</li>"
            "</ul>"
            "</p>")
        # pylint: enable-msg=R0801
        result: str = memorysize_conversion(memory_size)
        with allure.step(f"Pass memory size: {memorysize_conversion} "
                         f"and assert the result: {result} vs "
                         f"expected: {expected}"):

            print_log(memory_size=memory_size,
                      result=result,
                      expected=expected,
                      err=err)

            self.assertEqual(result, expected, msg=err)

    @parameterized.expand([
        ('1 KiB', 'kB', 1.024),
        ("1 MiB", "MB", 1.048576),
        ("1 GB", "GiB", 0.93132257461548)])
    def test_unit_extractor(self, memory_size, units_exp, ratio_exp):
        """
        Test 'unit_extractor' function with various test data.

        :param memory_size: str
        :param units_exp: str
        :param ratio_exp: float
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing 'unit_extractor' function:")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>"
            "Test a conversion function between the kB and "
            "the KiB-Units:"
            "<ul>"
            "<li>KiB -> kB, 1.024</li>"
            "<li>kB -> KiB, 0.9765625</li>"
            "</ul>"
            "etc..."
            "</p>")
        # pylint: enable-msg=R0801
        units, ratio = unit_extractor(memory_size)
        with allure.step(f"Pass memory size: {memorysize_conversion} "
                         f"and assert the units: {units} "
                         f" and ratio: {ratio}"):

            print_log(memory_size=memory_size,
                      units=units,
                      units_exp=units_exp,
                      ratio=ratio,
                      ratio_exp=ratio_exp)

            # assert units conversion
            self.assertEqual(units, units_exp)
            # assert ratio
            self.assertEqual(ratio, ratio_exp)
