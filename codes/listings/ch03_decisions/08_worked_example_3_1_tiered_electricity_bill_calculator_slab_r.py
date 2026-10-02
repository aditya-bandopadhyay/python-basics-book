# Making Decisions -- Worked Example 3.1: Tiered Electricity Bill Calculator (Slab Rates)
# (book source: ch03_decisions.tex, line 309)

units = 250
bill_amount = 0.0

if units <= 100:
    bill_amount = 0.0
elif units <= 200:
    bill_amount = (units - 100) * 5.0
else:
    # First 100 free + Next 100 @ Rs 5 (Rs 500) + Remaining @ Rs 8
    bill_amount = (100 * 5.0) + (units - 200) * 8.0

print(f"Units Consumed: {units} kWh")
print(f"Total Bill:     Rs {bill_amount:,.2f}")

# Output:
# Units Consumed: 250 kWh
# Total Bill:     Rs 900.00
