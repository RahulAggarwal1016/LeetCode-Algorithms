# Implementing a Hash Map
# Hash map avoids collisions by adding a list to each hash index (which is also a list)
class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        # check if hash index is empty
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            # check if key already exists (in that case update value)
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            # if key doesn't exist in occupied hash index, than just append
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
            # key does not exist
            return None

    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        print("-----PRINTING HASHMAP-----")
        for item in self.map:
            if item is not None:
                print(str(item))

# Hash Map Class using dictionaries to avoid collisions
