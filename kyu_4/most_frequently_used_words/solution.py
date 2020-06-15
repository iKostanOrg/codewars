"""Most frequently used words in a text"""


#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def top_3_words(text: str) -> list:
    """
    Given a string of text (possibly with punctuation and line-breaks),
    returns an array of the top-3 most occurring words, in descending
    order of the number of occurrences.

    :param text: a string of text
    :return: an array of the top-3 most occurring words
    """
    # 1
    # Matches should be case-insensitive, and the words
    # in the result should be lower-cased.
    illegals = ';/_?,.:!-'
    text_lower = text.lower()
    for char in illegals:
        text_lower = text_lower.replace(char, ' ')
    # 2
    words: list = [word for word in text_lower.split() if word.replace("'", '') != '']
    processed = set()
    # 3
    counters: dict = dict()
    for word in words:
        if word not in processed:
            processed.add(word)
            counter = words.count(word)
            if counter in counters:
                counters[counter].append(word)
            else:
                counters[counter] = [word]
    # 4
    results = list()
    n = 3
    keys = sorted(counters.keys(), reverse=True)
    for counter in keys:
        diff = n - len(results)
        results += counters[counter][:diff]

        if len(results) == 3:
            break

    return results
