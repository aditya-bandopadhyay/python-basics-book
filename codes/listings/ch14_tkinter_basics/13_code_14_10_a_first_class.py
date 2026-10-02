# Tkinter Basics -- Code 14.10: A first class
# (book source: ch14_tkinter_basics.tex, line 508)

class Counter:
    def __init__(self, start=0):     # runs when a new Counter is created
        self.count = start           # an attribute stored on this object

    def increment(self):             # a method: a function that belongs
        self.count += 1              # to the class

    def reset(self):
        self.count = 0

a = Counter()          # a new object; __init__ runs with start=0
a.increment()
a.increment()
b = Counter(10)        # a second, independent object
b.increment()
print(a.count, b.count)
a.reset()
print(a.count, b.count)

# Output:
# 2 11
# 0 11
