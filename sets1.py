a={1,2,3,4,5,6}
b={3,4,5,6,7,8}

c=a.union(b)#c=a|b this also used to union
print("Union of a and b is: ",c)

d=a.intersection(b)
print("Intersection of a and b is: ",d)

e=a.difference(b)#e=a-b
print("a-b is: ",e)

f=b.difference(a)#f=b-a
print("b-a is: ",f)

g=a.symmetric_difference(b)#g=a^b "common aa irukkirathai viddu mitchathai return pannum"
print("Symmetric difference of a and b is: ",g)