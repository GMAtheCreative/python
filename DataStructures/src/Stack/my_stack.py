
class StackEmptyException(Exception):
    pass

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1

    def pop(self):
        self.exception()
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        self.exception()
        return self.top.data

    def get_size(self):
        self.exception()
        return self.size

    def exception(self):
        if self.is_empty():
            raise StackEmptyException
