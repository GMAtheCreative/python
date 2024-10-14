
import unittest

from Stack.my_stack import Stack,StackEmptyException


class TestStack(unittest.TestCase):
    def test_stack_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())

    def test_element_can_be_pushed_to_stack(self):
        stack = Stack()
        stack.push(700)
        self.assertFalse(stack.is_empty())

    def test_element_can_be_popped(self):
        stack = Stack()
        stack.push(700)
        stack.push(300)
        stack.push(500)
        self.assertEqual(500, stack.pop())

    def test_elements_can_be_popped(self):
        stack = Stack()
        stack.push(700)
        stack.push(300)
        stack.push(500)
        stack.pop()
        stack.pop()
        self.assertEqual(700, stack.pop())

    def test_elements_can_be_peeked(self):
        stack = Stack()
        stack.push(700)
        stack.push(300)
        stack.push(500)
        stack.pop()
        self.assertEqual(300, stack.peek())

    def test_get_size_of_stack(self):
        stack = Stack()
        stack.push(700)
        stack.push(300)
        stack.push(500)
        self.assertEqual(3, stack.get_size())

    def test_stack_can_throw_exception_if_stack_is_empty(self):
        stack = Stack()
        with self.assertRaises(StackEmptyException):
            stack.peek()
        with self.assertRaises(StackEmptyException):
            stack.pop()
        with self.assertRaises(StackEmptyException):
            stack.get_size()
