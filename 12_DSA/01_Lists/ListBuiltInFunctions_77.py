subjects=["Maths","Tamil","Maths","English","ICT"]
subjects.insert(2,"Geography")#add geography in 2nd index
print(subjects)

subjects.append("Economics")#add in the end one element
print(subjects)

subjects.extend(["Music","Art"])#add in the end
print(subjects)

subjects.pop(2)#delete 2nd index
print(subjects)

subjects.pop()#delete last element
print(subjects)

pos=subjects.index("English")
print("POS",pos)
print("Index of English: ",pos)

count=subjects.count("Maths")#count the number of elements
print(count)
print("Maths occurs: ",count,"times")

print("Final list is: ",subjects)






#ListBuilInFunctions_77.py