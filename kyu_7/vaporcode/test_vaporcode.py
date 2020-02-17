#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# FUNDAMENTALS

import unittest
import allure
from utils.log_func import print_log
from kyu_7.vaporcode.vaporcode import vaporcode


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("String")
@allure.story('V A P O R C O D E')
@allure.tag()
@allure.link(url='',
             name='Source/Kata')
class VaporcodeTestCase(unittest.TestCase):
    """
    Testing 'vaporcode' function
    """

    def test_vaporcode(self):
        """
        Testing 'vaporcode' function
        :return:
        """

        allure.dynamic.title("Testing 'vaporcode' function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p></p>")

        with allure.step("Enter string with spaces"
                         " and verify the output"):
            s = "Lets go to the movies"
            expected = "L  E  T  S  G  O  T  O  " \
                       "T  H  E  M  O  V  I  E  S"

            print_log(s=s, expected=expected)
            self.assertEqual(vaporcode(s), expected)

        with allure.step("Enter string with special "
                         "chars and verify the output"):
            s = "Why isn't my code working?"
            expected = "W  H  Y  I  S  N  '  T  M  Y  " \
                       "C  O  D  E  W  O  R  K  I  N  G  ?"

            print_log(s=s, expected=expected)
            self.assertEqual(vaporcode(s), expected)

        with allure.step("Enter crazy string and verify the output"):
            s = " ; FUV! qd vz  Xy-b pM.!:F  lEqRLY,p RGS:;Rh Z "
            expected = ";  F  U  V  !  Q  D  V  Z  X  Y  -  B  P  " \
                       "M  .  !  :  F  L  E  Q  R  L  Y  ,  P  R  G  " \
                       "S  :  ;  R  H  Z"

            print_log(s=s, expected=expected)
            self.assertEqual(vaporcode(s), expected)

        with allure.step("Enter string with chars"
                         "only and verify the output"):
            s = "blah"
            expected = "B  L  A  H"

            print_log(s=s, expected=expected)
            self.assertEqual(vaporcode(s), expected)
