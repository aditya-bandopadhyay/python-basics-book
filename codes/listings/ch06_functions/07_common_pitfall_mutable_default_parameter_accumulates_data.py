# Functions and Code Reuse -- Common Pitfall: Mutable Default Parameter Accumulates Data
# (book source: ch06_functions.tex, line 358)

def add_item(val, container=[]):
    container.append(val)
    return container

print(add_item("Apple"))  # ['Apple']
print(add_item("Banana")) # ['Apple', 'Banana'] -> Accumulated unexpectedly!
