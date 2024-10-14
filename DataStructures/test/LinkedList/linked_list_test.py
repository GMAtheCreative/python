
import unittest
from LinkedList.linked_list import MyListException, MyList


class TestMyList(unittest.TestCase):

    def test_size_of_empty_list(self):
        my_list = MyList()
        self.assertEqual(len(my_list), 0)

    def test_add_element_to_empty_list(self):
        my_list = MyList()
        my_list.add(10)
        self.assertEqual(len(my_list), 1)
        self.assertEqual(my_list.peek(), 10)

    def test_add_element_to_non_empty_list(self):
        my_list = MyList()
        my_list.add(10)
        my_list.add(20)
        self.assertEqual(len(my_list), 2)
        self.assertEqual(my_list.peek(), 10)

    def test_add_at_index(self):
        my_list = MyList()
        with self.assertRaises(MyListException):
            my_list.add_at_index(0, 10)

        my_list.add(10)
        my_list.add_at_index(0, 20)
        self.assertEqual(len(my_list), 2)
        self.assertEqual(my_list.peek_at_index(0), 20)
        self.assertEqual(my_list.peek_at_index(1), 10)


    def test_remove_from_empty_list(self):
        my_list = MyList()
        with self.assertRaises(MyListException):
            my_list.remove()

    def test_remove_from_non_empty_list(self):
        my_list = MyList()
        my_list.add(10)
        my_list.remove()
        self.assertEqual(len(my_list), 0)

    def test_remove_at_index_from_empty_list(self):
        my_list = MyList()
        with self.assertRaises(MyListException):
            my_list.remove_at_index(0)

    def test_remove_at_index_from_non_empty_list(self):
        my_list = MyList()
        my_list.add(10)
        my_list.add(20)
        my_list.remove_at_index(0)
        self.assertEqual(len(my_list), 1)
        self.assertEqual(my_list.peek(), 20)

    def test_contains_in_empty_list(self):
        my_list = MyList()
        with self.assertRaises(MyListException):
            my_list.contains(10)

    def test_contains_in_non_empty_list(self):
        my_list = MyList()
        my_list.add(10)
        self.assertTrue(my_list.contains(10))

    def test_peek_from_empty_list(self):
        my_list = MyList()
        with self.assertRaises(MyListException):
            my_list.peek()

    def test_peek_from_non_empty_list(self):
        my_list = MyList()
        my_list.add(10)
        self.assertEqual(my_list.peek(), 10)

    def test_peek_at_index_from_empty_list(self):
        my_list = MyList()
        with self.assertRaises(MyListException):
            my_list.peek_at_index(0)

    def test_peek_at_index_from_non_empty_list(self):
        my_list = MyList()
        my_list.add(10)
        self.assertEqual(my_list.peek_at_index(0), 10)

    def test_index_out_of_bounds_exception(self):
        my_list = MyList()
        with self.assertRaises(MyListException):
            my_list.peek_at_index(1)

if __name__ == '__main__':
    unittest.main()
