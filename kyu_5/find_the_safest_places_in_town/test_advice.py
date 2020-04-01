#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

# ALGORITHMS

import unittest
import allure
from utils.log_func import print_log
from kyu_5.find_the_safest_places_in_town.advice import advice


@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("Algorithms")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Find the safest places in town')
@allure.tag('ALGORITHMS')
@allure.link(url='https://www.codewars.com/kata/5dd82b7cd3d6c100109cb4ed/train/python',
             name='Source/Kata')
class FirstNonRepeatingLetterTestCase(unittest.TestCase):
    """
    Testing advice function
    """

    def test_first_non_repeating_letter(self):
        """
        Testing a function named advice(agents, n) where:
            - agents is an array of agent coordinates.
            - n defines the size of the city that Bassi needs to hide in,
              in other words the side length of the square grid.

        The function should return a list of coordinates that are the furthest
        away (by Manhattan distance) from all agents.
        :return:
        """
        allure.dynamic.title("Testing advice function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p>The function should return a list of coordinates that "
                                        "are the furthest away (by Manhattan distance) from all agents.</p>")

        with allure.step("Enter test string and verify the output"):
            test_data = [
                ([(1, 1)], 2, [(0, 0)],
                 "Should return top left corner for agent in the bottom right"),
                ([(1, 1)], 0, [],
                 "Should return empty list for size 0"),
                ([(0, 0), (1, 5), (5, 1)], 6, sorted([(2, 2), (3, 3), (4, 4), (5, 5)]),
                 "Works for the example in description"),
                ([(9, 9)], 1, [(0, 0)],
                 "Should return all locations for only ignored agents"),
                ([(1, 1), (3, 5), (4, 8), (7, 3), (7, 8), (9, 1)], 10, sorted([(0, 9), (0, 7), (5, 0)]),
                 "Should return correct solutions for six agents"),
                ([(1, 3), (2, 3), (2, 7), (4, 1), (5, 9), (7, 0), (9, 5)], 10,
                 sorted([(0, 0), (0, 9), (4, 5), (5, 5), (5, 4), (6, 3), (6, 4), (6, 6), (7, 7), (8, 8), (9, 9)]),
                 "Should return correct solutions for seven agents"),
                ([(0, 0), (0, 9), (1, 5), (5, 1), (9, 0), (9, 9)], 10, sorted([(5, 7), (6, 6), (7, 5)]),
                 "Should return correct solutions for another six agents"),
                ([(0, 0)], 10, [(9, 9)],
                 "single agent in top left corner of large grid"),
                ([(0, 0), (1, 1), (99, 99)], 2, sorted([(0, 1), (1, 0)]),
                 "agent in top left and bottom right"),
            ]

            for data in test_data:
                agents = data[0]
                n = data[1]
                expected = data[2]
                message = data[3]
                print_log(agents=agents, n=n, expected=expected, message=message)
                self.assertEqual(expected,
                                 sorted(advice(agents=agents, n=n)),
                                 message)
