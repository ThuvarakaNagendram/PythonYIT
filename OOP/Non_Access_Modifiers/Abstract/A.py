from abc import ABC, abstractmethod

class A(ABC):
    x=10;
    
    @abstractmethod
    def getX(self):
        pass
