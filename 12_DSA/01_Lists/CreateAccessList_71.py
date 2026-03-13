subjects=["Maths","Science","Tamil","ICT","English"]
print("subjects:",subjects)
print("Type: ",type(subjects))
print(subjects[0])
print(subjects[-1])
print("Length:",len(subjects))
subjects[0]="Histry"
print("After added Histry to 0 index: ",subjects)
subjects.append("Physics")
print("After append physics",subjects)