"""D2: Days, hours, minutes and seconds in one million seconds."""
total_seconds = 1_000_000

days = total_seconds // 86400            # 86400 seconds in a day
remaining = total_seconds % 86400
hours = remaining // 3600
remaining = remaining % 3600
minutes = remaining // 60
seconds = remaining % 60

print(f"{total_seconds:,} seconds = {days} days, {hours} h, {minutes} min, {seconds} s")
# Output: 1,000,000 seconds = 11 days, 13 h, 46 min, 40 s
