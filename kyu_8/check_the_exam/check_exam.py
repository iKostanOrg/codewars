"""
Solution for -> Check the exam
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def check_exam(arr1, arr2) -> int:
    """
    The first input array contains the correct answers
    to an exam, like ["a", "a", "b", "d"]. The second
    one is "answers" array and contains student's answers.

    The two arrays are not empty and are the same length.
    Return the score for this array of answers, giving +4
    for each correct answer, -1 for each incorrect answer,
    and +0 for each blank answer(empty string).

    If the score < 0, return 0.

    :param arr1:
    :param arr2:
    :return:
    """
    results: list = []
    for char in zip(arr1, arr2):
        char_processor(char, results)

    total = sum(results)
    return 0 if total < 0 else total


def char_processor(char: str, results: list) -> None:
    """
    Processing chars based on specified rule
    :param char: str
    :param results: list
    :return: None
    """
    if char[1] == '':
        results.append(0)
    elif char[0] == char[1]:
        results.append(4)
    else:
        results.append(-1)
