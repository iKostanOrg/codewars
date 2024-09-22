"""
Node class for -> Fun with lists: length
Created by Egor Kostan.
GitHub: https://github.com/ikostan
"""


class Node:
    """
    The linked list
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
