class Map:
    def __init__(self):
        self.map = []

    def put(self, key, value):
        self.map.append((key, value))

    def get(self, key):
        for keys, values in self.map:
            if keys == key:
                return values
        return None

    def remove(self, key):
        self.map = [(keys, values) for keys, values in self.map if keys != key]

