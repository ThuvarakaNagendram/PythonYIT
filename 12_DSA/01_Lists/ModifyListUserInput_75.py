subjects=["Maths","Tamil","English","Science","ICT"]
i=0
while i<len(subjects):
    subjects[i]=input(f"Enter new subject for subject {i+1}:")
    i+=1
print("Updated list: ",subjects)