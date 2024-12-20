"""
Solution for -> Simple Fun #152: Invite More Women?.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def invite_more_women(arr: list) -> bool:
    """
    Invite More Women function.

    Arthur wants to make sure that there are at least as
    many women as men at this year's party. He gave you
    a list of integers of all the party goers.

    Arthur needs you to return true if he needs to invite
    more women or false if he is all set.

    An array representing the genders of the attendees,
    where -1 represents women and 1 represents men.
    :param arr:
    :return:
    """
    if not arr or arr == []:
        return False

    if sum(arr) <= 0:
        return False

    return True
