subject=["Maths","Science","Tamil","ICT", "Maths"]
print(subject)
#print(type(subject))
#print(subject[0])
#print(len(subject))
#subject[0]="Religion"
#print(subject)
subject.append("Physics")#add single element to the list
print(subject)

subject.insert(2,"Religion")# add in the notified index
print(subject)

subject.extend(["Chemistry","Biology"])#add multiple elements to the list
print(subject)

subject.pop()#remove the last element
print(subject)

subject.pop(2)#remove the notified element
print(subject)

print(subject.index("Tamil"))# print the index of the element

print(subject.count("Maths"))#find how many times the particular element is in the list

subject.remove("Science")
print(subject)

subject.clear()
print(subject)



"""
i=0
while i<len(subject):
    print(subject[i])
    i+=1
  
for s in subject:
    print(s)
    
subject[0]="English"
print(subject)

i=0
while i<len(subject):
    subject[i]=input(f"Which subject want to change for {subject[i]}: ")
    i+=1
print(subject)
"""
