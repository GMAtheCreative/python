import unittest

from set.my_set import MySet


class TestMySet(unittest.TestCase):
    def test_set_is_empty(self):
        my_set = MySet()
        self.assertTrue(my_set.is_empty())

    def test_add_element_to_set(self):
        my_set = MySet()
        my_set.add(200)
        my_set.add(300)
        self.assertEqual(my_set.get_size(), 2)

    def test_set_contains_element(self):
        my_set = MySet()
        my_set.add(200)
        my_set.add(300)
        self.assertTrue(my_set.contains(300))

    def test_set_doesnt_contain_element(self):
        my_set = MySet()
        my_set.add(200)
        my_set.add(300)
        self.assertFalse(my_set.contains(400))

    def test_add_collection(self):
        my_set = MySet()
        numbers = [1, 3, 7, 2, 9, 12]
        my_set.add_all(numbers)
        self.assertEqual(my_set.get_size(), 6)

    def test_remove_element_from_set(self):
        my_set = MySet()
        my_set.add(200)
        my_set.add(300)
        my_set.add(20)
        my_set.add(40)
        my_set.remove(40)
        self.assertEqual(my_set.get_size(), 3)
        self.assertFalse(my_set.contains(40))
