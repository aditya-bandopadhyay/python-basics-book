# Functions and Code Reuse -- Code 6.2: Local scope
# (book source: ch06_functions.tex, line 243)

def double(x):
    result = x * 2   # 'result' lives only inside double()
    return result

y = double(5)
print(y)       # Output: 10
# print(result)  # NameError: name 'result' is not defined
