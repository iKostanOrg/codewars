#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def check_exam(arr1, arr2):
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

    arr = zip(arr1, arr2)
    results = list()
    for char in arr:
        if char[1] == '':
            results.append(0)
        elif char[0] == char[1]:
            results.append(4)
        else:
            results.append(-1)

    total = sum(results)
    return 0 if total < 0 else total
