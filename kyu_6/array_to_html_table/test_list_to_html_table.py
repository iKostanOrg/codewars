"""
Test for -> Array to HTML table
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""

# FUNDAMENTALS ARRAYS

import unittest
import allure
from utils.log_func import print_log
from kyu_6.array_to_html_table.to_table import to_table


@allure.epic('6 kyu')
@allure.parent_suite('Novice')
@allure.suite("Fundamentals")
@allure.sub_suite("Unit Tests")
@allure.feature('Lists')
@allure.story('Array to HTML table')
@allure.tag('FUNDAMENTALS',
            'ARRAYS',
            'LISTS')
@allure.link(
    url='https://www.codewars.com/kata/5e7e4b7cd889f7001728fd4a/train/python',
    name='Source/Kata')
class ArrayToTableTestCase(unittest.TestCase):
    """
    Testing to_table function
    """

    def test_array_to_table_function(self):
        """
        Testing to_table with various test data
        :return:
        """
        # pylint: disable-msg=R0801
        allure.dynamic.title("Testing to_table function")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        allure.dynamic.description_html(
            '<h3>Codewars badge:</h3>'
            '<img src="https://www.codewars.com/users/myFirstCode'
            '/badges/large">'
            '<h3>Test Description:</h3>'
            "<p>Test that function takes three arguments "
            "(data, header, index) and returns a string "
            "containing HTML tags representing the table.</p>")
        # pylint: enable-msg=R0801
        test_data = ([
            {
                "input": ([["o"]]),
                "output": "<table><tbody>"
                          "<tr><td>o</td></tr>"
                          "</tbody></table>"
            },
            {
                "input": ([["lorem", "ipsum"], ["dolor", "sit amet"]], True, True),
                "output": "<table><thead>"
                          "<tr><th></th><th>lorem</th><th>ipsum</th></tr>"
                          "</thead><tbody>"
                          "<tr><td>1</td><td>dolor</td><td>sit amet</td></tr>"
                          "</tbody></table>"
            },
            {
                "input": ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], False, True),
                "output": "<table><tbody>"
                          "<tr><td>1</td><td>1</td><td>2</td><td>3</td></tr>"
                          "<tr><td>2</td><td>4</td><td>5</td><td>6</td></tr>"
                          "<tr><td>3</td><td>7</td><td>8</td><td>9</td></tr>"
                          "</tbody></table>"
            },
            {
                "input": (
                    [
                        ["id", "name", "price", "quantity"],
                        [24351, "pen", 2.41, 500],
                        [None, "pencil", 0.99, 25],
                        [63401, "grizzly bear", None, 1],
                        [3532, "rubber duck", 5.45, 24],
                        [1523, None, 3.00, 6.8],
                        [11765, "caviar", 67.95, None]
                    ], True),
                "output":
                    "<table><thead>"
                    "<tr><th>id</th><th>name</th><th>price</th><th>quantity</th></tr>"
                    "</thead>"
                    "<tbody>"
                    "<tr><td>24351</td><td>pen</td><td>2.41</td><td>500</td></tr>"
                    "<tr><td></td><td>pencil</td><td>0.99</td><td>25</td></tr>"
                    "<tr><td>63401</td><td>grizzly bear</td><td></td><td>1</td></tr>"
                    "<tr><td>3532</td><td>rubber duck</td><td>5.45</td><td>24</td></tr>"
                    "<tr><td>1523</td><td></td><td>3.0</td><td>6.8</td></tr>"
                    "<tr><td>11765</td><td>caviar</td><td>67.95</td><td></td></tr>"
                    "</tbody></table>"
            },
            {
                "input": ([["a", "b", "c", "d", "e"], [True, False, False, True, True]], True),
                "output": "<table><thead>"
                          "<tr><th>a</th><th>b</th><th>c</th><th>d</th><th>e</th></tr>"
                          "</thead>"
                          "<tbody>"
                          "<tr><td>True</td><td>False</td><td>False</td><td>True</td>"
                          "<td>True</td></tr>"
                          "</tbody></table>"
            },
        ])

        for test_item in test_data:
            data: list = test_item["input"][0]
            header = test_item["input"][1] if len(test_item["input"]) > 1 else False
            index: bool = test_item["input"][2] if len(test_item["input"]) > 2 else False
            expected = test_item["output"]
            actual_result = to_table(data, header, index)

            with allure.step("Enter a test data and verify the expected output vs actual result"):
                print_log(exp=expected, res=actual_result)
                self.assertEqual(expected, actual_result)


if __name__ == '__main__':
    unittest.main()
