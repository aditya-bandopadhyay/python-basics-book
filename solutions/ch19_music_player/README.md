# Chapter 19 — Desktop Audio Player and Frequency Visualizer — Solutions

## Multiple-choice answers

Q1: (c), Q2: (a), Q3: (c), Q4: (b), Q5: (a).

## Short-answer hints

- **S1.** With shuffle off, the next index is `(current_idx + 1) % len(tracks)`, which wraps from the last track to the first. With shuffle on, a random index is chosen with `random.randint(0, len(tracks) - 1)`. ``Previous'' always steps back by one.
- **S2.** `time.sleep()` blocks the main thread, so Tkinter's event loop cannot redraw the window or react to clicks; the window freezes. `root.after()` schedules the next frame and returns immediately.
- **S3.** The slider's `command` callback receives the new value as a string; convert it with `float()`, store it as the playback position, and update the elapsed-time label with a `MM:SS` formatting function.

## Exercise solutions

| Exercise | File | What it shows |
| --- | --- | --- |
| DIY D1 | [`diy_1.py`](diy_1.py) | D1: Volume slider plus a Mute button that remembers the previous level. |
| DIY D2 | [`diy_2.py`](diy_2.py) | D2: Repeat button cycling Off -> Repeat All -> Repeat One. |
| DIY D3 | [`diy_3.py`](diy_3.py) | D3: Dropdown to switch the visualizer colour palette. |
| DIY D4 | [`diy_4.py`](diy_4.py) | D4: Peak-hold markers: a white line above each bar that falls slowly. |
| Debugging Bugs 1–5 | [`bugs_fixed.py`](bugs_fixed.py) | Bugs 19.1-19.5, fixed. |
| Mini-Project | [`mini_project.py`](mini_project.py) | Mini-Project 19: Audio synthesizer and waveform studio. |

Helper module(s) used by the solutions above: `_app.py`.
