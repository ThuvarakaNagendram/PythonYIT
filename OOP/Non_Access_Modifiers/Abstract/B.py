from A import A

class B(A):
    y=20
    
    def getY(self):
        print("By is: ",self.y)
        
    def getX(self):
        print("Ax is: ",self.x)
    