class P02_Robot:
    pass
x=P02_Robot()
y=P02_Robot()
x.name="Yoha"
x.year=1987
y.name="Seelan"
y.age=39

print(x.name)#Yoha
print(x.year)#1987
print(y.name)#Seelan
print(y.age)#39

print(x.__dict__)#{'name': 'Yoha', 'year': 1987}