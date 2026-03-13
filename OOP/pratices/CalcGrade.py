class CalcGrade:
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
        
    def isTopper(self,grade):
        if(grade=='A'):
            isTop='U r topper'
        else:
            isTop='Better luck next time'
        return isTop               
        
    def display(self):
        total=self.calcTotal()
        average=self.calcAverage(total)
        grade=self.getGrade(average)
        isTop=self.isTopper(grade)
        print("My id is: ",self.id)
        print("My name is: ",self.name)
        print("Marks are in order: ",self.m1,self.m2,self.m3)
        print("Total is: ",total)
        print("Average is: ",average)  
        print("Grade is :",grade)
        print("Hi,",isTop)
         
student1=CalcGrade(1,"Seelan")
student1.setMarks(85,85,85)
student1.display()
