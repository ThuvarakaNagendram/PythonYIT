num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
selection=int(input("Selection range: \n\t1 is for Addition \n\t2 is for Substraction \n\t3 is for Multiplication \n\t4 is for Devision \nEnter your selection range: "))
match selection:
    case 1:
        addition=num1+num2
        print("Addition of",num1, "and",num2, "is: ",addition)
    case 2:
        substraction=num1-num2
        print("Substraction of",num1, "and",num2, "is: ",substraction)        
    case 3:
        multiplication=num1*num2
        print("Multiplication of",num1, "and",num2, "is: ",multiplication)
    case 4:
        devision=num1/num2
        print("Devision of",num1, "and",num2, "is: ",devision)
    case _:
        print("Invalid range")

    
