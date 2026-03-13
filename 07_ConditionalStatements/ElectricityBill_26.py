print("Electricity Bill Calculator")
unit=int(input("Enter the electricity units: "))

if unit>=0:
    if 1<=unit<=90:
        bill=unit*7
        
    elif 91<=unit<=150:
        bill=(90*7)+(unit-90)*10
        
    elif 151<=unit<=300:
        bill=(90*7)+(60*10)+(unit-150)*15
        
    else:
        bill=(90*7)+(60*10)+(150*15)+(unit-300)*15
        additionalCharge=bill*0.003
        bill=bill+additionalCharge
        print("Additional charge 3% applied")
        
    print("Total bill is :",bill)
    
else:
    print("Invalid input")