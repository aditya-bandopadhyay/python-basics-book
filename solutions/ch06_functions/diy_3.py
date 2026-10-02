"""D3: Count the words in a sentence."""

def word_count(sentence):
    """Return the number of words (split at any run of spaces)."""
    return len(sentence.split())

print(word_count("The quick brown fox"))        # Output: 4
print(word_count("  spaces   everywhere  "))    # Output: 2
print(word_count(""))                            # Output: 0
