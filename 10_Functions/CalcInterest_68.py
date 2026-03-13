def calcInterest(amount,period):
    if period==0.25:
        interest=amount*12/100
    elif period==0.5:
        interest=amount*12.5/100
    elif period==1:
        interest=amount*13/100
    elif period==3:
        interest=amount*14/100
    elif period==5:
        interest=amount*15/100
    elif period>5:
        interest=amount*15.5/100
    else:
        print("Invalid period")
        
    total=amount+interest
    print(f"Interest:{interest} Total amount:{total}")
    
calcInterest(10000,5)

"""
def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

amount = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (%): "))
period = float(input("Enter the period (in years): "))

si = calculate_interest(amount, rate, period)

print("Simple Interest is:", si)
print("Total Amount after", period, "years is:", amount + si)
"""