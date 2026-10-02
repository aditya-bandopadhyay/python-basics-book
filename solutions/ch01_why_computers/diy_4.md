# D4: Flowchart, "is N divisible by 5?"

```
        ( Start )
            |
   /  Read integer N  /          <- parallelogram (input)
            |
     < N % 5 == 0 ? >            <- decision diamond
       /          \
     Yes           No
     |              |
 / Print        / Print            <- parallelograms (output)
 "Divisible  /   "Not divisible
  by 5"         by 5"  /
       \          /
         ( Stop )                <- terminator
```

The same logic in Python (Chapter 3 teaches `if`):

```python
N = int(input("Enter a whole number: "))
if N % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")
```
