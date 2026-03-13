class StudentFullName:
    
    def __init__(self,fName,lName,id):#parameterConstructor
        self.fName = fName
        self.lName=lName
        self.id = id
        
    def display(self):#default
        print("My id is:", self.id)
        print("My first name is:", self.fName)
        print("My last name is:",self.lName)        
        print("My fullname is "+self.getFullName())
        
    def getFullName(self):#return method
        return self.fName+self.lName


stu1 = StudentFullName("Yoha","Seelan",1000)
stu1.display()

