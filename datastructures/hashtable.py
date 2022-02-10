from linkedlist import LinkedList


class HashElement:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __eq__(self, __o: object) -> bool:
        return self.key == __o

    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)


class Hash:
    def __init__(self, size=16, max_load_factor=.75):
        self.size = size
        self.number_of_elements = 0
        self._positions = [LinkedList() for _ in range(self.size)]
        self.max_load_factor = max_load_factor

    def load_factor(self):
        return self.number_of_elements / self.size

    def resize(self, size):
        new_positions = [LinkedList() for _ in range(size)]
        for key in self:
            val = self.get(key)
            hash_val = (hash(key) & 0x7FFFFFFF) % size
            new_positions[hash_val].append(HashElement(key, val))
        self._positions = new_positions
        self.size = size

    def hash_func(self, key):
        hash_val = hash(key)
        hash_val = hash_val & 0x7FFFFFFF
        return hash_val % self.size

    def add(self, key, value):
        if self.load_factor() > self.max_load_factor:
            self.resize(self.size * 2)

        hash_val = self.hash_func(key)

        self._positions[hash_val].append(HashElement(key, value))
        self.number_of_elements += 1
        return True

    def remove(self, key):
        hash_val = self.hash_func(key)
        self._positions[hash_val].remove(key)
        self.number_of_elements -= 1
        return True

    def get(self, key):
        hash_val = self.hash_func(key)
        for element in self._positions[hash_val]:
            if element.key == key:
                return element.val
        return None
    
    def __iter__(self):
        return HashIterator(self)


class HashIterator:
    def __init__(self, hash):
        self.keys = []
        self.pos = -1

        for i in range(hash.size):
            for element in hash._positions[i]:
                self.keys.append(element.key)

    def has_next(self):
        return self.pos < len(self.keys) - 1

    def __next__(self):
        if not self.has_next():
            raise StopIteration
        
        self.pos += 1
        return self.keys[self.pos]

