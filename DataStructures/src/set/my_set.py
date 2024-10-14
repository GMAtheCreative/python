
class MySetException(Exception):
    pass

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MySet:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        self.exception()
        return self.size

    def add(self, data):
        if not self.contains(data):
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def contains(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def add_all(self, data):
        for value in data:
            self.add(value)

    def remove(self, data):
        self.exception()
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return
        current = self.head
        previous = None
        while current is not None:
            if current.data == data:
                previous.next = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

    def exception(self):
        if self.head is None:
            raise MySetException

