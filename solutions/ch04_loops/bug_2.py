"""Bug 4.2 -- n grows forever, so 'n > 0' never becomes False.

Fix: start where you want to count from and move n TOWARDS the stopping
condition. Counting down from 5 to 1:
"""
n = 5
while n > 0:
    print(n)
    n -= 1
