
import unittest

from Queue.my_queue import QueueIsEmptyException,Queue


class TestQueue(unittest.TestCase):
    def test_queue_is_empty(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())

    def test_queue_can_add_element(self):
        queue = Queue()
        queue.enqueue(17)
        self.assertFalse(queue.is_empty())

    def test_queue_can_add_another_element(self):
        queue = Queue()
        queue.enqueue(17)
        queue.enqueue(18)
        self.assertEqual(queue.get_size(), 2)

    def test_queue_can_add_more_elements(self):
        queue = Queue()
        queue.enqueue(17)
        queue.enqueue(18)
        queue.enqueue(19)
        queue.enqueue(20)
        self.assertEqual(queue.get_size(), 4)

    def test_queue_can_remove_element(self):
        queue = Queue()
        queue.enqueue(17)
        queue.enqueue(18)
        queue.enqueue(19)
        self.assertEqual(queue.dequeue(), 17)

    def test_queue_can_throw_exception_if_queue_is_empty(self):
        queue = Queue()
        with self.assertRaises(QueueIsEmptyException):
            queue.dequeue()

    def test_queue_can_remove_another_element(self):
        queue = Queue()
        queue.enqueue(17)
        queue.enqueue(18)
        queue.enqueue(19)
        queue.enqueue(20)
        self.assertEqual(queue.dequeue(), 17)
        self.assertEqual(queue.dequeue(), 18)
        self.assertEqual(queue.get_size(), 2)

    def test_queue_can_peek_to_check_first_element(self):
        queue = Queue()
        queue.enqueue(17)
        queue.enqueue(18)
        queue.enqueue(19)
        self.assertEqual(queue.peek(), 17)

    def test_queue_can_peek_after_dequeuing(self):
        queue = Queue()
        queue.enqueue(17)
        queue.enqueue(18)
        queue.enqueue(19)
        self.assertEqual(queue.peek(), 17)
        self.assertEqual(queue.dequeue(), 17)
        self.assertEqual(queue.peek(), 18)

    def test_peek_can_throw_exception_if_queue_is_empty(self):
        queue = Queue()
        with self.assertRaises(QueueIsEmptyException):
            queue.peek()
