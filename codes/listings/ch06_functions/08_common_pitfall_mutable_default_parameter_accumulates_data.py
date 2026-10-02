# Functions and Code Reuse -- Common Pitfall: Mutable Default Parameter Accumulates Data
# (book source: ch06_functions.tex, line 367)

def add_item(val, container=None):
    if container is None:
        container = []
    container.append(val)
    return container
