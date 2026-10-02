# Chapter 3 — Making Decisions — Solutions

## Multiple-choice answers

Q1: (b), Q2: (c), Q3: (b), Q4: (b), Q5: (b).

## Short-answer hints

- **S1.** Indentation defines the block structure of conditional branches. Statements aligned under the same level of indentation are executed together inside that conditional branch.
- **S2.** In independent `if` statements, every condition is evaluated separately (multiple blocks can execute). In an `if-elif-else` chain, evaluation stops at the first matching branch (only one block executes).
- **S3.** A single `=` assigns (stores a value): `score = 100`. A double `==` compares and gives `True` or `False`: `if score == 100:`.

## Exercise solutions

| Exercise | File | What it shows |
| --- | --- | --- |
| DIY D1 | [`diy_1.py`](diy_1.py) | D1: Positive, negative, or zero. |
| DIY D2 | [`diy_2.py`](diy_2.py) | D2: Letter grade from a percentage. |
| DIY D3 | [`diy_3.py`](diy_3.py) | D3: Traffic light (Code 3.2) with a check for unknown colours. |
| DIY D4 | [`diy_4.py`](diy_4.py) | D4: Leap-year checker, tested with 2024, 2000, 1900 and 2023. |
| Debugging Bug 1 | [`bug_1.py`](bug_1.py) | Bug 3.1 -- a single = assigns; comparisons need >= (or ==). |
| Debugging Bug 2 | [`bug_2.py`](bug_2.py) | Bug 3.2 -- the body of an if must be indented. |
| Debugging Bug 3 | [`bug_3.py`](bug_3.py) | Bug 3.3 -- 'age >= 0' is true for every real age, so the or-condition is always True. |
| Debugging Bug 4 | [`bug_4.py`](bug_4.py) | Bug 3.4 -- the two messages are swapped. |
| Debugging Bug 5 | [`bug_5.py`](bug_5.py) | Bug 3.5 -- the boundary 10 belongs to Medium, but 'number > 10' excludes it. |
| Mini-Project | [`mini_project.py`](mini_project.py) | Mini-Project 3: Number guessing game (one guess; Chapter 4 adds a loop). |
