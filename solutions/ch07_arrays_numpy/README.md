# Chapter 7 — Scientific Arrays with NumPy — Solutions

## Multiple-choice answers

Q1: (b), Q2: (c), Q3: (b), Q4: (b), Q5: (b).

## Short-answer hints

- **S1.** NumPy arrays store data in contiguous memory blocks and use vectorized operations compiled in C, bypassing Python's element-wise loop overhead.
- **S2.** The `shape` tuple lists the dimensions of the array. Use `arr.reshape(3, 4)` on a 1-D array of 12 elements to transform it into a $3 4$ array.
- **S3.** Element-wise arithmetic applies mathematical operations to corresponding elements. For example, adding two NumPy arrays `A + B` computes the sum at each index, rather than concatenating them.

## Exercise solutions

| Exercise | File | What it shows |
| --- | --- | --- |
| DIY D1 | [`diy_1.py`](diy_1.py) | D1: sin^2 + cos^2 = 1 on 50 points from 0 to 2*pi. |
| DIY D2 | [`diy_2.py`](diy_2.py) | D2: 4x4 matrix with entry i*j, built by broadcasting. |
| DIY D3 | [`diy_3.py`](diy_3.py) | D3: k-point running mean, with a loop and with np.convolve. |
| DIY D4 | [`diy_4.py`](diy_4.py) | D4: Benchmark a Python loop against np.sum on a million numbers. |
| Debugging Bug 1 | [`bug_1.py`](bug_1.py) | Bug 7.1 -- ** is not defined for Python lists (TypeError). |
| Debugging Bug 2 | [`bug_2.py`](bug_2.py) | Bug 7.2 -- M[1] is ROW 1, not column 1. |
| Debugging Bug 3 | [`bug_3.py`](bug_3.py) | Bug 7.3 -- shapes (3,) and (4,) cannot be broadcast: the trailing sizes differ |
| Debugging Bug 4 | [`bug_4.py`](bug_4.py) | Bug 7.4 -- M[1] picks a single row. |
| Debugging Bug 5 | [`bug_5.py`](bug_5.py) | Bug 7.5 -- b = a does not copy the array; both names refer to the same data. |
| Mini-Project | [`mini_project.py`](mini_project.py) | Mini-Project 7: Signal generator -- mean, peak and RMS, with and without noise. |
