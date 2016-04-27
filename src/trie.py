# _*_ encoding: utf-8 _*_


class Trie(object):
    """Create a Trie."""
    def __init__(self):
        self.root = {}

    def insert(self, token):
        """Insert word into the Trie."""
        if not token or not isinstance(token, str):
            return
        cur = self.root
        for letter in token:
            cur = cur.setdefault(letter, {})
        cur['$'] = '$'

    def contains(self, token):
        """Check if word is in the Trie."""
        if not token or not isinstance(token, str):
            return False
        cur = self.root
        token += '$'
        for letter in token:
            try:
                cur = cur[letter]
            except KeyError:
                return False
        return True

    def traversal(self, start=None, word=''):
        """Generator that yields all the words in the Trie."""
        start = start or self.root
        for key in start.keys():
            if key == '$':
                yield word
            else:
                for thing in self.traversal(start[key], word + key):
                    yield thing
