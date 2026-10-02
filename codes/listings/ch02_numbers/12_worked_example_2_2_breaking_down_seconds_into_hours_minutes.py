# Playing with Numbers -- Worked Example 2.2: Breaking Down Seconds into Hours, Minutes, and Seconds
# (book source: ch02_numbers.tex, line 443)

total_seconds = 7542

# Step 1: Calculate hours (3600 seconds in 1 hour)
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

# Step 2: Calculate minutes and leftover seconds (60 seconds in 1 minute)
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{total_seconds} seconds = {hours}h {minutes}m {seconds}s")
# Output: 7542 seconds = 2h 5m 42s
