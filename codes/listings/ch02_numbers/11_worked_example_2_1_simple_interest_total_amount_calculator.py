# Playing with Numbers -- Worked Example 2.1: Simple Interest & Total Amount Calculator
# (book source: ch02_numbers.tex, line 411)

# Step 1: Input values
principal = 50000.0     # Principal in Rupees
rate_percent = 7.5      # Annual interest rate in %
time_years = 3.0        # Time duration in years

# Step 2: Calculate Simple Interest and Total Amount
simple_interest = (principal * rate_percent * time_years) / 100.0
total_amount = principal + simple_interest

# Step 3: Print the formatted results
print(f"Principal Deposit: Rs {principal:,.2f}")
print(f"Simple Interest:   Rs {simple_interest:,.2f}")
print(f"Total Amount:      Rs {total_amount:,.2f}")

# Output:
# Principal Deposit: Rs 50,000.00
# Simple Interest:   Rs 11,250.00
# Total Amount:      Rs 61,250.00
