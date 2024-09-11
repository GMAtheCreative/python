import unittest
from new_array.arrays import array_function


class TestArray(unittest.TestCase):
    def test_that_function_can_take_in_an_array_and_return_the_amount_of_odd_and_even(self):
        array_intake = array_function([1,2,3,4,5,6,7,8])
        self.assertEqual(array_intake, [4,4])
