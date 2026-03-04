
name = ["Ammu","Pommu","Athi"]
subjects = ["Maths","Science","Tamil"]
marks = [[98,87,78],[78,68,94],[76,83,91]]

print("Student Name\tMaths\tScience\tTamil\tTotal\tAverage\tGrade")
#print(f"{'StudentName':>15}{'Maths':<8}{'Tamil':<10}{'Total':<10}{'Average':<10}{'Grade':<10}")

for i in range(len(name)):#row
    
    total = 0
    
    print(name[i], end="\t\t")
    
    for j in range(len(subjects)):#for each subject mark
        print(marks[i][j], end="\t")
        total += marks[i][j]
    
    average = total / len(subjects)
    
    if average >= 75:
        grade = "A"
    elif average >= 65:
        grade = "B"
    elif average >= 55:
        grade = "C"
    elif average>=45:
        grade= "S"
    else:
        grade = "D"
    
    print(total, end="\t")
    print(f"{average:.2f}", end="\t")
    print(grade)