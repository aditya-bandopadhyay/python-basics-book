"""Mini-Project 2: Rupee currency converter."""
USD_RATE = 0.012     # US dollars per rupee (example rates; check today's values)
EUR_RATE = 0.011
GBP_RATE = 0.0095

rupees = float(input("Amount in Indian Rupees: "))

usd_amount = rupees * USD_RATE
eur_amount = rupees * EUR_RATE
gbp_amount = rupees * GBP_RATE

print(f"Rs {rupees:,.2f} is:")
print(f"  US Dollars:     $ {usd_amount:.2f}")
print(f"  Euros:          EUR {eur_amount:.2f}")
print(f"  British Pounds: GBP {gbp_amount:.2f}")
