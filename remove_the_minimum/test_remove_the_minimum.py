import unittest
from remove_the_minimum.remove_the_minimum import remove_smallest
from numpy.random import randint

# FUNDAMENTALS LISTS DATA STRUCTURES ARRAYS


class RemoveSmallestTestCase(unittest.TestCase):
    """
    Testing remove_smallest function
    """

    @staticmethod
    def random_list():
        """
        Helper function
        :return:
        """
        return list(randint(400, size=randint(1, 10)))

    def test_remove_smallest(self):
        """
        Test lists with multiple digits
        :return:
        """
        
        self.assertEqual(remove_smallest([1, 2, 3, 4, 5]),
                         [2, 3, 4, 5],
                         "Wrong result for [1, 2, 3, 4, 5]")

        self.assertEqual(remove_smallest([5, 3, 2, 1, 4]),
                         [5, 3, 2, 4],
                         "Wrong result for [5, 3, 2, 1, 4]")

        self.assertEqual(remove_smallest([1, 2, 3, 1, 1]),
                         [2, 3, 1, 1],
                         "Wrong result for [1, 2, 3, 1, 1]")

    def test_remove_smallest_empty_list(self):
        """
        Test with empty list
        :return:
        """
        self.assertEqual(remove_smallest([]),
                         [],
                         "Wrong result for []")

    def test_remove_smallest_one_element_list(self):
        """
        Returns [] if list has only one element
        :return:
        """
        for i in range(10):
            x = randint(1, 400)
            self.assertEqual(remove_smallest([x]),
                             [],
                             "Wrong result for [{}]".format(x))

    def test_remove_smallest_random_list(self):
        """
        Returns a list that misses only one element
        :return:
        """

        for i in range(10):
            arr = self.random_list()
            self.assertEqual(len(remove_smallest(arr[:])),
                             len(arr) - 1,
                             "Wrong sized result for {}".format(arr))
