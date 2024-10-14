
class MyListException(Exception):
    pass

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1

    def add_at_index(self, index, data):
        self.index_out_of_bounds_exception(index)
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def add_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def remove(self):
        self.exception()
        self.head = self.head.next
        self.size -= 1

    def remove_at_index(self, index):
        self.exception()
        self.index_out_of_bounds_exception(index)
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

    def contains(self, data):
        self.exception()
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def peek(self):
        self.exception()
        return self.head.data

    def peek_at_index(self, index):
        self.exception()
        self.index_out_of_bounds_exception(index)
        if index == 0:
            return self.head.data
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current.data

    def index_out_of_bounds_exception(self, index):
        if index < 0 or index >= self.size:
            raise MyListException("Index out of bounds")

    def exception(self):
        if self.head is None:
            raise MyListException()
