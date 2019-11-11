#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def pig_it(text: str) -> str:
    """
    Move the first letter of each word to the end of it,
    then add "ay" to the end of the word. Leave
    punctuation marks untouched.
    :param text:
    :return:
    """
    result = list()
    for word in text.split(' '):
        if len(word) > 1:
            result.append('{}ay'.format(word[1:] + word[0]))
        elif len(word) == 1 and word.isalpha():
            result.append('{}ay'.format(word))
        else:
            result.append(word)

    return ' '.join(result)
