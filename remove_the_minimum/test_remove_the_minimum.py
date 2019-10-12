import unittest
from remove_the_minimum.remove_the_minimum import remove_smallest
from numpy.random import randint

# FUNDAMENTALS LISTS DATA STRUCTURES ARRAYS


class RemoveSmallestTestCase(unittest.TestCase):
    """
    Testing remove_smallest function
    """

    @staticmethod
    def randlist():
        """
        Helper function
        :return:
        """
        return list(randint(400, size=randint(1, 10)))

    def test_something(self):
        self.assertEqual(True, False)
        self.assertEqual(remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]")
        self.assertEqual(remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4], "Wrong result for [5, 3, 2, 1, 4]")
        self.assertEqual(remove_smallest([1, 2, 3, 1, 1]), [2, 3, 1, 1], "Wrong result for [1, 2, 3, 1, 1]")
        self.assertEqual(remove_smallest([]), [], "Wrong result for []")



    Test.it("returns [] if list has only one element")
    for i in range(10):
        x = randint(1, 400)
        Test.assert_equals(remove_smallest([x]), [], "Wrong result for [{}]".format(x))

    Test.it("returns a list that misses only one element")
    for i in range(10):
        arr = randlist()
        Test.assert_equals(len(remove_smallest(arr[:])), len(arr) - 1, "Wrong sized result for {}".format(arr))
