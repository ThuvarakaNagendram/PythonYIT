from B import B
from C import C

class HierarchicalDefault:
    b=B()
    b.getX()
    b.getY()
    
    c=C()
    c.getX()
    c.getZ()