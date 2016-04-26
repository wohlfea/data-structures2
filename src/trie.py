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

    def traversal(self, start=None, word=''):
        if not start:
            start = self.root
        end = False
        keys = start.keys()
        if '$' in keys:
            keys.remove('$')
            end = True
        for key in keys:
            for thing in self.traversal(start[key], word + key):
                yield thing
        if end:
            yield word
    # def traversal(self, start=None, word=''):
    #     if not start:
    #         start = self.root
    #     keys = start.keys()
    #     if word:
    #         if word[-1] == '$':
    #             yield word[:-1]
    #     for key in keys:
    #         for word in self.traversal(start[key], word + key):
    #             yield word
