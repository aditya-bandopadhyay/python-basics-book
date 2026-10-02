"""D2: Read 5 names into a list and print them sorted."""
names = []
for i in range(5):
    names.append(input(f"Name {i + 1}: ").strip())
print(sorted(names))
# Note: sorted() puts capital letters before lower-case ones.
# sorted(names, key=str.lower) ignores case.
