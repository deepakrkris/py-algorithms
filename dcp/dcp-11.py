from library.trie import Trie

WORDS = ['foo', 'bar', 'dog', 'deer', 'deal']

def autocomplete(s):
  results = set()
  for word in WORDS:
      if word.startswith(s):
          results.add(word)

  return results

print(autocomplete('de'))

trie = Trie()
for word in WORDS:
    trie.insert(word)

def autocompleteTrie(s):
    return trie.elements(s)

print(autocompleteTrie('de'))
