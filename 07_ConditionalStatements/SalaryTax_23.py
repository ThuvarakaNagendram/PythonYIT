employeeName=input("Enter your name: ")
salary=int(input("Enter your salary: "))
if(salary>=100000):
    tax=0.05*salary
    netSalary=salary-tax
    #print("Hello",employeeName,"\n5% deduction of your salary is",tax, "\nYour Net salary is: "+str(netSalary))
elif(salary<100000 and salary>=80000):
    tax=0.03*salary
    netSalary=salary-tax
    #print("Hello",employeeName,"\n3% deduction of your salary is",tax, "\nYour Net salary is: "+str(netSalary))
elif(salary>0 and salary<=80000):
    #print("Hello",employeeName, "!\nYour Net salary is: "+str(salary))
else:
    print("Invalid range")
    
print("Hello",employeeName,"\ndeduction of your salary is",tax,"\nYour Net salary is ",netSalary)

