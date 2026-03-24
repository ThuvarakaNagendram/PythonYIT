class A:
    def __init__(self):
        self.x=10
    
    def getX(self):
        print("Ax: ",self.x)
        
class B(A):
    def __init__(self):
        super().__init__()
        self.y=20
    
    def getY(self):
        print("By: ",self.y)
        
b=B()
b.getX()
b.getY()


        
