# Code from the book

Every program in the book is here, in two forms. They contain the **same code**; use
whichever is more convenient.

## 1. `listings/` -- one file per listing (matches the book exactly)

Each chapter has a folder, and each code listing in that chapter is its own file, in the
order it appears in the book. The file name includes the listing's number and title, and
the first comment line repeats the title exactly as printed:

```
codes/listings/ch02_numbers/08_code_2_3_formatted_output_with_f_strings.py   <- Code 2.3
```

The leading number (`08_`) is only the position in the chapter: chapters also contain
unnumbered examples (Try It boxes, Common Mistake boxes, the Real-World Solution), and
these get files too. A few listings are fragments or deliberate mistakes shown in the book;
their files say so in a `NOTE` comment at the top.

## 2. `chNN_*.py` -- one script per chapter

- **Chapters 1-13:** all of the chapter's listings joined into one script that runs from
  top to bottom, with a banner before each listing. Listings that need keyboard input or
  are deliberate mistakes are skipped (the banner says where to find them).
- **Chapters 14-19:** the chapter's main desktop application (for example the log
  calculator in Chapter 16). The other programs from those chapters are in `listings/`.

## Running

Run everything from the repository root, so that paths like `data/grades.csv` work:

```bash
python codes/listings/ch02_numbers/08_code_2_3_formatted_output_with_f_strings.py
python codes/ch02_numbers.py
```
