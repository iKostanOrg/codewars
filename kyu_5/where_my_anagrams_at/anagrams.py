#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def anagrams(word, words):
    """
    A function that will find all the anagrams of a word
    from a list. You will be given two inputs a word and
    an array with words. You should return an array of all
    the anagrams or an empty array if there are none.
    """

    template = sorted([char for char in word])
    results = list()

    for w in words:
        if template == sorted([char for char in w]):
            results.append(w)

    return results
