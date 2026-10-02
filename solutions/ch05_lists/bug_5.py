"""Bug 5.5 -- the first time a word is seen, counts[w] does not exist yet.

Reading counts[w] for a missing key raises KeyError. Start each new word at 0
(or use counts.get(w, 0)).
"""
words = "the cat and the dog".split()
counts = {}
for w in words:
    if w in counts:
        counts[w] = counts[w] + 1
    else:
        counts[w] = 1
print(counts)   # Output: {'the': 2, 'cat': 1, 'and': 1, 'dog': 1}
