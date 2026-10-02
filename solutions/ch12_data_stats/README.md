# Chapter 12 — Data Wrangling and Statistics — Solutions

## Multiple-choice answers

Q1: (b), Q2: (c), Q3: (a), Q4: (b), Q5: (b).

## Short-answer hints

- **S1.** There are 6 combinations out of 36 yielding a sum of 7, compared to only 1 combination ($1+1$) yielding a sum of 2.
- **S2.** Simpson's Paradox occurs when an unobserved confounding variable (such as patient disease severity) is unequally distributed across subgroups. Aggregating the data produces a weighted average dominated by unequal group allocations, reversing the true trend present within every individual subgroup.
- **S3.** Simulate draws using `np.random.choice()` without replacement and compute the fraction of trials where both drawn items match the red target.

## Exercise solutions

| Exercise | File | What it shows |
| --- | --- | --- |
| DIY D1 | [`diy_1.py`](diy_1.py) | D1: mode(data) that reports every value in a tie. |
| DIY D2 | [`diy_2.py`](diy_2.py) | D2: Pearson r from scratch vs np.corrcoef on y = 2x + noise. |
| DIY D3 | [`diy_3.py`](diy_3.py) | D3: Bootstrap 95% confidence interval for a mean. |
| DIY D4 | [`diy_4.py`](diy_4.py) | D4: Statistics and outliers for data/marks.csv. Run from the repository root. |
| Debugging Bug 1 | [`bug_1.py`](bug_1.py) | Bug 12.1 -- variance is the mean of the SQUARED DEVIATIONS (x - mu)**2, |
| Debugging Bug 2 | [`bug_2.py`](bug_2.py) | Bug 12.2 -- cov / cov is always 1. Divide by the product of the standard deviations. |
| Debugging Bug 3 | [`bug_3.py`](bug_3.py) | Bug 12.3 -- np.var is the variance; the standard deviation is its square root. |
| Debugging Bug 4 | [`bug_4.py`](bug_4.py) | Bug 12.4 -- np.corrcoef(x) correlates x with itself (1.0). Pass both arrays and |
| Debugging Bug 5 | [`bug_5.py`](bug_5.py) | Bug 12.5 -- axis=1 works ALONG each row (one result per row). |
| Mini-Project | [`mini_project.py`](mini_project.py) | Mini-Project 12: Class report for data/grades.csv. Run from the repository root. |
