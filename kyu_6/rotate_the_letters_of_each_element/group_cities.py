"""
Solution for -> ROTATE THE LETTERS OF EACH ELEMENT
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def group_cities(seq: list) -> list:
    """
    A function that given a sequence of strings, groups the elements
    that can be obtained by rotating others, ignoring upper or lower cases.

    In the event that an element appears more than once in the input
    sequence, only one of them will be taken into account for the result,
    discarding the rest.

    :param seq: Sequence of strings. Valid characters for those
                strings are uppercase and lowercase characters
                from the alphabet and whitespaces.
    :return: Sequence of elements. Each element is the group of
             inputs that can be obtained by rotating the strings.
    """
    results: list = []

    for item in seq:
        if len(results) == 0:
            temp: set = set()
            temp.add(item)
            results.append(temp)
            continue

        found: bool = False
        for sublist in results:
            for element in sublist:
                conditions = (len(element) == len(item),
                            sorted(element.lower()) == sorted(item.lower()),
                            rotate(item, element))
                if all(conditions):
                    sublist.add(element)
                    sublist.add(item)
                    found = True
                    break
        if not found:
            temp = set()
            temp.add(item)
            results.append(temp)

    # Sort the elements of each group alphabetically.
    results: list = ([sorted(list(r)) for r in results])
    # Sort the groups
    sort_results(results)
    return results


def rotate(item: str, element: str) -> bool:
    """
    Rotate elements/chars
    :param item: str
    :param element: str
    :return: bool
    """
    item: str = item.lower()
    element: str = element.lower()
    i: int = 0
    max_i = len(item) * len(item)
    while i < max_i:
        item = f'{item[1:]}{item[0]}'
        if item == element:
            return True
        i += 1
    return False


def sort_results(results: list) -> None:
    """
    Sort the groups deafeningly by size and in the case of a tie,
    by the first element of the group alphabetically.
    :param results: list
    :return: None
    """
    is_sorted: bool = False
    while not is_sorted:
        is_sorted = True
        for i, element in enumerate(results):
            if i + 1 < len(results):
                # Sort the groups deafeningly by size
                if len(element) < len(results[i + 1]):
                    is_sorted = False
                    results[i], results[i + 1] = results[i + 1], element
                # in the case of a tie, by the first element of the group alphabetically
                elif len(element) == len(results[i + 1]):
                    if results[i][0] > results[i + 1][0]:
                        is_sorted = False
                        results[i], results[i + 1] = results[i + 1], element
