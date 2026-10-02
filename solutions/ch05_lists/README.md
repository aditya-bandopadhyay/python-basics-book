# Chapter 5 — Lists, Tuples, Sets, and Dictionaries — Solutions

## Multiple-choice answers

Q1: (c), Q2: (c), Q3: (b), Q4: (c), Q5: (b).

## Short-answer hints

- **S1.** Lists are mutable, defined with `[]`, and suited for homogeneous, dynamic data. Tuples are immutable, defined with `()`, and faster/safer for heterogeneous, read-only data.
- **S2.** List indices are sequential integers starting at 0. Dictionary keys are key-value mappings that can be any immutable/hashable type (e.g., strings) and are non-sequential.
- **S3.** Sets do not allow duplicate values, which makes casting a list to a set an easy way to clean duplicates. Sets also use hash tables, enabling $O(1)$ constant-time membership testing.

## Exercise solutions

| Exercise | File | What it shows |
| --- | --- | --- |
| DIY D1 | [`diy_1.py`](diy_1.py) | D1: Celsius list with Fahrenheit equivalents. |
| DIY D2 | [`diy_2.py`](diy_2.py) | D2: Read 5 names into a list and print them sorted. |
| DIY D3 | [`diy_3.py`](diy_3.py) | D3: Remove duplicates, keeping the first appearance and the order. |
| DIY D4 | [`diy_4.py`](diy_4.py) | D4: Countries and capitals. |
| Debugging Bug 1 | [`bug_1.py`](bug_1.py) | Bug 5.1 -- a list of 5 items has indices 0..4, so scores[5] is out of range. |
| Debugging Bug 2 | [`bug_2.py`](bug_2.py) | Bug 5.2 -- 'count = 1' resets the counter instead of adding to it. |
| Debugging Bug 3 | [`bug_3.py`](bug_3.py) | Bug 5.3 -- list.remove() raises ValueError if the item is not in the list. |
| Debugging Bug 4 | [`bug_4.py`](bug_4.py) | Bug 5.4 -- dictionary keys are case-sensitive: "france" is not "France". |
| Debugging Bug 5 | [`bug_5.py`](bug_5.py) | Bug 5.5 -- the first time a word is seen, counts[w] does not exist yet. |
| Mini-Project | [`mini_project.py`](mini_project.py) | Mini-Project 5: Class report card. |
