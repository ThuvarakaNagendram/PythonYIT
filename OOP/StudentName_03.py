class StudentName:
    
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
    def display(self):
        print("My name is:", self.name)
        print("My id is:", self.id)


stu1 = StudentName("Seelan",1000)
stu1.display()

