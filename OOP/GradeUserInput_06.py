class GradeUserInput_06:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        
    def setMarks(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        
    def calcTotal(self):
        total=self.m1+self.m2+self.m3
        return total
        
    def calcAverage(self,total):
        average=total/3
        return average
        
    def getGrade(self,avrg):
        if(avrg>=75 and avrg<=100):
            result='A'
        elif(avrg>=65):
            result='B'
        elif(avrg>=55):
            result='C'
        elif(avrg>=35):
            result='S'
        elif(avrg>=0):
            result='W'
        else:
            result='Invalid range'
        return result
        
    def display(self):
        total=self.calcTotal()
        average=self.calcAverage(total)
        grade=self.getGrade(average)

        print("My id is:",self.id)
        print("My name is:",self.name)
        print("Marks are in order:",self.m1,self.m2,self.m3)
        print("Total is:",total)
        print("Average is:",average)
        print("Grade is:",grade)

id=int(input("Enter student id: "))
name=input("Enter student name: ")

#have to do the validation

m1=int(input("Enter mark 1: "))
m2=int(input("Enter mark 2: "))
m3=int(input("Enter mark 3: "))

student1=GradeUserInput_06(id,name)
student1.setMarks(m1,m2,m3)
student1.display()
