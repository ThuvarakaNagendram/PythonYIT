unit=int(input("Enter your unit: "))
if(unit>0 and unit<=90):
    amount=unit*7
elif(unit>90 and unit<=150):
    remain=unit-90
    amount=(90*7)+(remain*10)
elif(unit>150 and unit<=300):
    remain1=unit-150
    #remain2=150-remain1
    amount=(90*7)+(10*60)+(remain1*15)
elif(unit>300):
    remain2=unit-300
    totalAmount=(90*7)+(10*60)+(150*15)+(remain2*15)
    tax=totalAmount*0.3
    amount=totalAmount+tax
else:
    print("Invalid")
print("Your EBill amount is: ",amount)
    