"""
t=(10,20,30,40,50)
print(t)
print(type(t))
print(t[2])
t[2]==80
print(t[2])
print(t)
"""

"""
immutable
ordered
indexing
duplicate
"""

marks=[82,90,68,25,76]
t=tuple(marks)
print(t)
print(type(t))

marks1=(75,80,60)
marks2=(62,85,80)
marks3=marks1+marks2
print(marks3)