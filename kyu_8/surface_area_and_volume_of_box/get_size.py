"""
Solution for -> Surface Area and Volume of a Box.

Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


def get_size(w: int, h: int, d: int) -> list:
    """
    Return the total surface area and volume of a box as an array.

    :param w:
    :param h:
    :param d:
    :return:
    """
    volume: int = w * h * d
    # Source: http://www.webmath.com/geo_box.html
    area = 2 * (h * w) + 2 * (h * d) + 2 * (w * d)
    return [area, volume]
