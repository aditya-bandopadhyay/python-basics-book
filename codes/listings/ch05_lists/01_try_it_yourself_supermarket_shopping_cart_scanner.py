# Lists, Tuples, Sets, and Dictionaries -- Try It Yourself: Supermarket Shopping Cart Scanner
# (book source: ch05_lists.tex, line 39)

cart = [45.0, 120.5, 35.0, 250.0, 85.0]

print(f"Total Items:       {len(cart)}")
print(f"Total Bill Amount: Rs {sum(cart):.2f}")
print(f"Most Expensive:    Rs {max(cart):.2f}")
print(f"Cheapest Item:     Rs {min(cart):.2f}")
print(f"Sorted Bill:       {sorted(cart)}")
