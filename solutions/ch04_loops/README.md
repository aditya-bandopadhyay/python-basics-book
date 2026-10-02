# Chapter 4 — Loops and Repetition — Solutions

## Multiple-choice answers

Q1: (b), Q2: (b), Q3: (c), Q4: (b), Q5: (c).

## Short-answer hints

- **S1.** The `break` statement immediately terminates the loop. The `continue` statement skips only the remaining statements of the current iteration and jumps directly to the next loop cycle.
- **S2.** Use a `for` loop when iterating over a known sequence or range. Use a `while` loop when the number of iterations depends on a dynamic condition evaluated at runtime.
- **S3.** An infinite loop has a condition that never becomes `False`. Avoid it by ensuring the variables in the loop condition are modified inside the loop body.

## Exercise solutions

| Exercise | File | What it shows |
| --- | --- | --- |
| DIY D1 | [`diy_1.py`](diy_1.py) | D1: Multiplication table of 7. |
| DIY D2 | [`diy_2.py`](diy_2.py) | D2: First power of 2 that exceeds 1000, found with a while loop. |
| DIY D3 | [`diy_3.py`](diy_3.py) | D3: Sum of integers from 1 to 100 divisible by 3 or 5. |
| DIY D4 | [`diy_4.py`](diy_4.py) | D4: Right-angled triangle of stars. |
| Debugging Bug 1 | [`bug_1.py`](bug_1.py) | Bug 4.1 -- range(10) gives 0..9, so the sum is 45 instead of 55. |
| Debugging Bug 2 | [`bug_2.py`](bug_2.py) | Bug 4.2 -- n grows forever, so 'n > 0' never becomes False. |
| Debugging Bug 3 | [`bug_3.py`](bug_3.py) | Bug 4.3 -- the list has 3 items (indices 0, 1, 2) but range(4) also asks for index 3. |
| Debugging Bug 4 | [`bug_4.py`](bug_4.py) | Bug 4.4 -- break leaves the whole loop at the first negative number. |
| Debugging Bug 5 | [`bug_5.py`](bug_5.py) | Bug 4.5 -- i never changes, so 'i < 5' is always True: an infinite loop printing 0. |
| Mini-Project | [`mini_project.py`](mini_project.py) | Mini-Project 4: FizzBuzz from 1 to 100. |
