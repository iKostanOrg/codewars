#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import unittest
import allure
from utils.log_func import print_log
from kyu_5.sports_league_table_ranking.compute_ranks import compute_ranks


@allure.epic('5 kyu')
@allure.parent_suite('Novice')
@allure.suite("ALGORITHMS")
@allure.sub_suite("Unit Tests")
@allure.feature("Lists")
@allure.story('Sports League Table Ranking')
@allure.tag('ALGORITHMS', 'FUNDAMENTALS', 'ARRAYS', 'SORTING')
@allure.link(url='https://www.codewars.com/kata/5e0baea9d772160032022e8c/train/python',
             name='Source/Kata')
class ComputeRanksTestCase(unittest.TestCase):

    def test_something(self):
        """
        Test the function that organizes a sports league in a
        round-robin-system. Each team meets all other teams.
        In your league a win gives a team 2 points, a draw gives
        both teams 1 point. After some games you have to compute
        the order of the teams in your league. You use the following
        criteria to arrange the teams:

        - Points
        - Scoring differential (the difference between goals scored and those conceded)
        - Goals scored
        :return:
        """

        allure.dynamic.title("Testing compute_ranks")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html('<h3>Codewars badge:</h3>'
                                        '<img src="https://www.codewars.com/users/myFirstCode'
                                        '/badges/large">'
                                        '<h3>Test Description:</h3>'
                                        "<p>Test the function taht organizes a sports league in a "
                                        "round-robin-system. Each team meets all other teams. "
                                        "In your league a win gives a team 2 points, a draw gives "
                                        "both teams 1 point. After some games you have to compute "
                                        "the order of the teams in your league. You use the following "
                                        "criteria to arrange the teams:</p>"
                                        "<ul><li>- Points</li>"
                                        "<li>- Scoring differential (the difference between goals "
                                        "scored and those conceded)</li>"
                                        "<li>- Goals scored</li></ul>")

        test_data = [
            (6,
             [[0, 5, 2, 2],
              [1, 4, 0, 2],
              [2, 3, 1, 2],
              [1, 5, 2, 2],
              [2, 0, 1, 1],
              [3, 4, 1, 1],
              [2, 5, 0, 2],
              [3, 1, 1, 1],
              [4, 0, 2, 0]],
             [4, 4, 6, 3, 1, 2]),
            (6,
             [[0, 5, 2, 0],
              [1, 4, 2, 2],
              [2, 3, 1, 3],
              [1, 5, 0, 0],
              [2, 0, 2, 1],
              [3, 4, 3, 1]],
             [2, 3, 4, 1, 5, 6]),
            (4,
             [[0, 3, 1, 1],
              [1, 2, 2, 2],
              [1, 3, 2, 0],
              [2, 0, 2, 0]],
             [3, 1, 1, 3]),
            (10,
             [],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
            (8,
             [[0, 7, 2, 0]],
             [1, 2, 2, 2, 2, 2, 2, 8])
        ]

        for data in test_data:
            number = data[0]
            games = data[1]
            expected = data[2]
            actual_result = compute_ranks(number, games)
            print_log(number=number,
                      games=games,
                      expected=expected,
                      actual_result=actual_result)

            with allure.step("Enter a test data and verify the result:"):
                self.assertEqual(expected, actual_result)
