"""
Solution for -> Coloured Triangles
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


COLORS = {
    'R': 'R',
    'RR': 'R',
    'BG': 'R',
    'GB': 'R',
    'B': 'B',
    'BB': 'B',
    'RG': 'B',
    'GR': 'B',
    'G': 'G',
    'GG': 'G',
    'BR': 'G',
    'RB': 'G',
}


def triangle(row: str) -> str:
    """
    You will be given the first row of the triangle as a string
    and its your job to return the final colour which would
    appear in the bottom row as a string. I

    :param row: str, the first row of the triangle as a string
    :return: str, return the final colour
    """
    if len(row) < 2:
        return row

    while len(row) > 1:
        row_list = list(c for c in row)
        row = ''

        for i in range(len(row_list) - 1):
            key = ''.join(row_list[i: i + 2])
            row += COLORS[key]

    return row
