"""
Test for -> Make Class
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# ALGORITHMS GAMES OBJECT-ORIENTED PROGRAMMING

import unittest
import allure
from kyu_7.make_class.animal import Animal
from kyu_7.make_class.make_class import make_class
from utils.log_func import print_log


@allure.epic('7 kyu')
@allure.parent_suite('Beginner')
@allure.suite("OOP")
@allure.sub_suite("Unit Tests")
@allure.feature("Classes")
@allure.story('Make Class')
@allure.tag('ALGORITHMS',
            'GAMES',
            'OBJECT-ORIENTED PROGRAMMING')
@allure.link(
    url='https://www.codewars.com/kata/523f5d21c841566fde000009/train/python',
    name='Source/Kata')
# @pytest.mark.skip(reason="The solution is not ready")
class MakeClassTestCase(unittest.TestCase):
    """
    Testing make_class function
    """
    def test_make_class(self):
        """
        Testing make_class function
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing make_class function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Give me the power to create a similar class like this:</p>"
            "<p>Animal = make_class(\"name\", \"species\", \"age\", \"health\", "
            "\"weight\", \"color\")</p>")
        # pylint: enable-msg=R0801
        with allure.step("Test class creation by using a function"):

            Animel = make_class("name",
                                "species",
                                "age",
                                "health",
                                "weight",
                                "color")

            dog1 = Animal(name="Bob",
                          species="Dog",
                          age=5,
                          health="good",
                          weight="50lb",
                          color="brown")

            dog2 = Animel(name="Bob",
                          species="Dog",
                          age=5,
                          health="good",
                          weight="50lb",
                          color="brown")

            test_data = ((dog1.name, dog2.name),
                         (dog1.species, dog2.species),
                         (dog1.age, dog2.age),
                         (dog1.health, dog2.health),
                         (dog1.weight, dog2.weight),
                         (dog1.color, dog2.color))

            for td in test_data:
                a = td[0]
                b = td[1]

                with allure.step(f"Assert that classes {a} and "
                                 f"{b} have equal properties"):
                    print_log(a=a, b=b)
                    self.assertEqual(a, b)
