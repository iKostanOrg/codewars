#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


class Node:
    """
    The linked list
    """

    def __init__(self, data, next=None):
        self.data = data
        self.next = next
