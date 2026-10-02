"""Bug 3.5 -- the boundary 10 belongs to Medium, but 'number > 10' excludes it.

With number = 10 the buggy program prints Small. Use >= 10 instead.
(100 is handled correctly: it is not > 100, and it is >= 10, so Medium.)
"""
for number in [5, 10, 100, 150]:
    if number > 100:
        label = "Large"
    elif number >= 10:
        label = "Medium"
    else:
        label = "Small"
    print(number, label)
# Output:
# 5 Small
# 10 Medium
# 100 Medium
# 150 Large
