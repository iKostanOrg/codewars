#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def get_size(w, h, d) -> list:
    """
    Write a function that returns the total surface
    area and volume of a box as an array: [area, volume]
    :param w:
    :param h:
    :param d:
    :return:
    """

    volume = w * h * d
    # Source: http://www.webmath.com/geo_box.html
    area = 2 * (h * w) + 2 * (h * d) + 2 * (w * d)

    return [area, volume]
