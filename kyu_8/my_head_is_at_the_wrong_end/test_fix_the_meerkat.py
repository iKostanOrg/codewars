#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS ARRAYS LISTS DATA STRUCTURES

import unittest
import allure
import pytest


@allure.epic('8 kyu')
@allure.parent_suite('Beginner')
@allure.suite("Data Structures")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('My head is at the wrong end!')
@allure.tag('ALGORITHMS', 'ARRAYS', 'LISTS', 'DATA STRUCTURES')
@allure.link(url='https://www.codewars.com/kata/56f699cd9400f5b7d8000b55/train/python',
             name='Source/Kata')
@pytest.mark.skip(reason="The solution is not ready")
class FixTheMeerkatTestCase(unittest.TestCase):
    """
    Testing fix_the_meerkat function
    """

    def test_fix_the_meerkat(self):
        pass
