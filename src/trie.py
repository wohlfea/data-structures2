# _*_ encoding: utf-8 _*_
import itertools

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
        return bool(self._get_key_value(token, '$'))

    def _get_key_value(self, token, limiter=''):
        """Return word if in Trie."""
        if not token or not isinstance(token, str):
            return
        cur = self.root
        token += limiter
        for letter in token:
            try:
                cur = cur[letter]
            except KeyError:
                return
        return cur

    def traversal(self, start=None, word=''):
        """Generator that yields all the words in the Trie."""
        start = start or self.root
        for key in start.keys():
            if key == '$':
                yield word
            else:
                for thing in self.traversal(start[key], word + key):
                    yield thing

    def autocomplete(self, token):
        """Return up to 4 suggested words based on input."""
        output = {}
        # import pdb; pdb.set_trace()
        for idx, char in enumerate(token):
            search = token[:idx + 1]
            cur = self._get_key_value(search)
            generator = self.traversal(cur, search)

            output[search] = list(itertools.islice(generator, 4))
        return output



