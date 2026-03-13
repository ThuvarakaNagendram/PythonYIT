class P01_Robot:
    pass
if __name__=="__main__":
    x=P01_Robot()#here we are creating two different objects from class P01_Robot.
    y=P01_Robot()
    y1=y
    print(y==y1)
    print(x==y)#Even though they are from the same class, they are not the same object.
    print(x==y1)#Even though they are from the same class, they are not the same object.
