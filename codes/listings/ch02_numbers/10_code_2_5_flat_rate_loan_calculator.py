# Playing with Numbers -- Code 2.5: Flat-Rate Loan Calculator
# (book source: ch02_numbers.tex, line 381)

# Monthly payment on a flat-rate loan (interest charged on the full amount)
principal = 120000.0   # Total loan amount in Rupees
interest_rate = 0.08   # 8% annual interest rate
years = 5              # Loan duration in years

total_interest = principal * interest_rate * years
total_payable = principal + total_interest
monthly_payment = total_payable / (years * 12)

print(f"Total Interest:    Rs {total_interest:,.2f}")
print(f"Total Amount Due:  Rs {total_payable:,.2f}")
print(f"Monthly Payment:   Rs {monthly_payment:,.2f}")

# Output:
# Total Interest:    Rs 48,000.00
# Total Amount Due:  Rs 168,000.00
# Monthly Payment:   Rs 2,800.00
