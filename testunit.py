import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        print("average")
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        print("average1")
        self.assertRaises(ZeroDivisionError, average, [])
        print("error ")
        self.assertRaises(TypeError, average, 20, 30, 70)

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

unittest.main() # Calling from the command line invokes all tests