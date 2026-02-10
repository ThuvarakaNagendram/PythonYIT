
mark=int(input("Enter your marks:"))
if(mark>=75 and mark<=100):
    print("Your grade is A")
elif(mark>=65 and mark<75):
    print("Your grade is B")
elif(mark>=55 and mark<65):
    print("Your grade is C")
elif(mark>=35 and mark<55):
    print("Your grade is S")
elif(mark>=0 and mark<35):
    print("Sorry, better luck next time")
else:
    print("Invalid marks range, please check")

"""
    
mark=int(input("Enter your marks:"))
if (mark>=75 and mark<=100):
    print("Your grade is A")
elif(mark>=65):
    print("Your grade is B")
elif(mark>=55):
    print("Your grade is C")
elif(mark>=35):
    print("Your grade is S")
else:
    print("Sorry, better luck next time")
"""