def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

amount = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (%): "))
period = float(input("Enter the period (in years): "))

si = calculate_interest(amount, rate, period)

print("Simple Interest is:", si)
print("Total Amount after", period, "years is:", amount + si)
