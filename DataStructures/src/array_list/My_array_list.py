class ArrayList:

    def __init__(self, initial_capacity=10):
        self.capacity = initial_capacity
        self.size = 0
        self.array = [None] * self.capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize()
        self.array[self.size] = value
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if self.size == self.capacity:
            self._resize()
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.array[index]

    def set(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.array[index] = value

    def _resize(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def __str__(self):
        return str(self.array[:self.size])
