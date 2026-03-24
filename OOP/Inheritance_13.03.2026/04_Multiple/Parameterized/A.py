from B import B
from C import C

class A(B,C):
    def __init__(self,x,y,z):
        B.__init__(self,y)
        C.__init__(self,z)
        self.x=x
        
    def getX(self):
        print("Ax: ",self.x)