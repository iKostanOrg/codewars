#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def sentencify(words):
    """
    The function should:

    1. Capitalise the first letter of the first word.
    2. Add a period (.) to the end of the sentence.
    3. Join the words into a complete string, with spaces.
    4. Do no other manipulation on the words.

    :param words:
    :return:
    """
    return words[0][0].upper() + ' '.join(words)[1:] + '.'
