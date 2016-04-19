# _*_ encoding: utf-8 _*_


class HashTable(object):
    """Create an instance of a hash table."""

    def __init__(self, length):
        """Initialize with a certain size of table."""
        self.buckets = [[] for x in range(length)]

    def get(self, key):
        """Return the value stored with the given key."""
        # location = self._hash(key)
        for tup in self.buckets[self._hash(key)]:
            if tup[0] == key:
                return tup[1]

    def set(self, key, val):
        """Store the given val using the given key."""
        if not isinstance(key, str):
            raise TypeError('The key must be a string.')
        # location = self._hash(key)
        self.buckets[self._hash(key)].append((key, val))

    def _hash(self, key):
        """Hash the key provided."""
        return sum(ord(char) for char in key) % len(self.buckets)
        # TODO make better hashing to avoid collisions
