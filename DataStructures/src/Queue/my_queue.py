
class QueueIsEmptyException(Exception):
    pass

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def get_size(self):
        return self.size

    def dequeue(self):
        self.exception()
        data = self.front.data
        self.front = self.front.next
        if self.is_empty():
            self.rear = None
        self.size -= 1
        return data

    def peek(self):
        self.exception()
        return self.front.data

    def exception(self):
        if self.is_empty():
            raise QueueIsEmptyException
