
def factorial():
    i=int(input("Enter the number to be find factorial: "))
    fact=1
    for i in range(1,i+1):
        fact=fact*i
    print("Factorial of ",i,"is ",fact)
factorial()

"""
def factorial():
    num = int(input("Enter the number to find factorial: "))
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    print("Factorial of", num, "is:", fact)

factorial()
"""