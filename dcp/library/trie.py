ENDS_HERE = 'ENDS HERE'

class Trie(object):
    def __init__(self):
        self._trie = {}

    def insert(self, text):
        trie = self._trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[ENDS_HERE] = True


    def elements(self, prefix):
        trie = self._trie
        result = []

        for char in prefix:
            if char in trie:
                trie = trie[char]
            else:
                return []

        self.collect(trie, prefix, result)

        return result


    def collect(self, trie, prefix, result):

        for k,v in trie.items():
            if k == ENDS_HERE:
                result.append(prefix)
            else:
                self.collect(trie[k], prefix + k, result)

