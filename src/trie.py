# _*_ encoding: utf-8 _*_


class Trie(object):
    """Create a Trie."""
    def __init__(self):
        self.root = {}

    def insert(self, token):
        if not token or not isinstance(token, str):
            return
        cur = self.root
        for letter in token:
            cur = cur.setdefault(letter, {})
        cur['$'] = '$'

    def contains(self, token):
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
