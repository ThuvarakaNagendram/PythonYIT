#f-string
id=1001
name="Seelan"
age=22
print(f"My id is {id}\nMy name is {name}\nMy age is {age}")

#str.format()
id=1001
name="Seelan"
age=22
print("My id is {0} \nMy name is {1} \nMy age is {2}".format(id,name,age))

#str.format()in different order
id=1001
name="Seelan"
age=22
print("My id is {2} \nMy name is {0} \nMy age is {1}".format(name,age,id))

#using %
id=1001
name="Seelan"
age=22
print("My id is %d \nMy name is %s \nMy age is %d"%(id,name,age))