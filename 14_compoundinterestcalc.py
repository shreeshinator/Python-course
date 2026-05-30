principle = float(input("Enter the principal amount: "))

while principle <= 0:
    print("Principal amount must be greater than zero. Please enter a valid amount.")
    principle = float(input("Enter the principal amount: "))

rate = float(input("Enter the annual interest rate (in %): "))
while rate <= 0 or rate >= 100:
    print("Interest rate must be greater than zero and less than 100. Please enter a valid rate.")
    rate = float(input("Enter the annual interest rate (in %): "))

time = float(input("Enter the time in years: "))
while time <= 0:
    print("Time must be greater than zero. Please enter a valid time.")
    time = float(input("Enter the time in years: "))


# Calculate compound interest
amount = principle * (1 + rate / 100) ** time
compound_interest = amount - principle
print(f"Compound Interest: {compound_interest:.2f}")
print(f"Total Amount: {amount:.2f}")