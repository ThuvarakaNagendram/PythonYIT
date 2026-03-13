x=[[10,20,30],[40,70,80],[25,35,16]]
i = 0
while i < len(x):#rows
    j = 0
    while j < len(x[i]):#columns
        print(f"x[{i}][{j}] : {x[i][j]}")
        j += 1
    print("********************")
    i += 1