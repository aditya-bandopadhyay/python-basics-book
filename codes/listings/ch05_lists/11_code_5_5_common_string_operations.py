# Lists, Tuples, Sets, and Dictionaries -- Code 5.5: Common string operations
# (book source: ch05_lists.tex, line 499)

s = "The quick brown fox"

print(len(s))              # number of characters
print(s[0], s[-3:])        # first character, last three
print(s.upper())           # new string in capitals
print(s.replace("quick", "slow"))
print("fox" in s)          # is this text inside s?
print(s.count("o"))        # how many times "o" appears

words = s.split()          # break at spaces -> list of words
print(words)
print("-".join(words))     # glue a list back together

name = "  Asha  "
print("[" + name.strip() + "]")   # remove spaces at both ends

# Output:
# 19
# T fox
# THE QUICK BROWN FOX
# The slow brown fox
# True
# 2
# ['The', 'quick', 'brown', 'fox']
# The-quick-brown-fox
# [Asha]
