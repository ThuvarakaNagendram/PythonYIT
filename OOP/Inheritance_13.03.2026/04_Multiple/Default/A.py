from B import B
from C import C

class A(B,C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        self.x=10
        
    def getX(self):
        print("Ax: ",self.x)