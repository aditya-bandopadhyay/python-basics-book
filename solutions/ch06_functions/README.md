# Chapter 6 — Functions and Code Reuse — Solutions

## Multiple-choice answers

Q1: (c), Q2: (b), Q3: (c), Q4: (b), Q5: (b).

## Short-answer hints

- **S1.** Parameters are the variable names listed in the function's definition. Arguments are the actual values passed to the function when it is called.
- **S2.** Docstrings document function purpose and arguments for other programmers or help systems. They should be written as a triple-quoted string immediately after the function signature line.
- **S3.** Scope determines where a variable is accessible. Local variables are defined inside a function and are only accessible within it. Global variables are defined at the module root level.

## Exercise solutions

| Exercise | File | What it shows |
| --- | --- | --- |
| DIY D1 | [`diy_1.py`](diy_1.py) | D1: Kilometres <-> miles, checked with a marathon distance. |
| DIY D2 | [`diy_2.py`](diy_2.py) | D2: is_prime(n) from Worked Example 4.2, used to list primes up to 50. |
| DIY D3 | [`diy_3.py`](diy_3.py) | D3: Count the words in a sentence. |
| DIY D4 | [`diy_4.py`](diy_4.py) | D4: FizzBuzz as a function. |
| Debugging Bug 1 | [`bug_1.py`](bug_1.py) | Bug 6.1 -- the function computes result but never returns it. |
| Debugging Bug 2 | [`bug_2.py`](bug_2.py) | Bug 6.2 -- Python runs a script top to bottom, so square() does not exist yet |
| Debugging Bug 3 | [`bug_3.py`](bug_3.py) | Bug 6.3 -- 'return' is indented inside the loop, so the function returns |
| Debugging Bug 4 | [`bug_4.py`](bug_4.py) | Bug 6.4 -- 'total' is a local variable of compute(); it vanishes when the |
| Debugging Bug 5 | [`bug_5.py`](bug_5.py) | Bug 6.5 -- countdown() calls itself forever: there is no base case. |
| Mini-Project | [`mini_project.py`](mini_project.py) | Mini-Project 6: A small statistics library written with plain Python. |
