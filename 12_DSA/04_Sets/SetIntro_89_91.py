s={"Maths","Science","Tamil","ICT","Maths","Science","History"}
print(s)
print(type(s))
print(len(s))

s.add("English")#add only one element to the set
print(s)

s.remove("Science")
print(s)

s.discard("Science")
print(s)

s.update(["Physics","Chemistry","Biology"])#add multi value
print(s)

s.pop()
print(s)

my_sub=["Religion","Geogra"]
s.update(my_sub)
print(s)

s.clear()
print(s)



"""
Unordered
unchangeable
duplicates not allowed
"""