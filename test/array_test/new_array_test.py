import unittest

from new_array.arrays import array_function


class MyTestCase(unittest.TestCase):
    def test_that_function_can_take_in_an_array_and_return_the_amount_of_odd_and_even(self):
        array_intake = array_function([4, 1, 5, 7])
        self.assertEqual([3,1], array_intake)  # add assertion here


