print("Level 1 – Basic")
print("01:")
s = ("abc")
print("\nfor x in s:") 
for x in s:
    print(x)
 
print("\nfor x in range(len(s)):") 
for x in range(len(s)):
    print(x)

print("\nfor index in range(len(s)):")   
for index in range(len(s)):
    print(s[index])
    
"""x = "GFG" 
for i in range(x):
    print(i)# this gives error bcs"""
    
print("\n02:")
print("Iterating by Index of Sequences")
li = ["geeks", "for", "geeks"]
for index in range(len(li)):
    print(li[index])
    
print("\n03:")
print("Print numbers from 1 to 10")
for x in range(1,11):
    print(x)
    
print("\n04:")
print("Print even numbers from 1 to 20")
for x in range(0,21,2):
    print(x)
    
print("\n05:")
print("Print odd numbers from 1 to 20")
for x in range(1,20,2):
    print(x)
    
print("\n06:")
print("Print numbers from 10 to 1 (reverse order)")
for x in range(10,0,-1):
    print(x)
    
print("Level 2 – With Conditions")

print("\n07:")
print("Print numbers from 1 to 50 that are divisible by 5")
for x in range(0,51,5):
    print(x)
print("or else...........")
for x in range(0,51):
    if(x%5==0):
        print(x)
        
print("\n08:")
print("Print the square of numbers from 1 to 10")
for x in range(1,11):
    print(x*x)
    
print("Level 3 – Using Input")
    
print("\n09:")
print("Find the sum of numbers from 1 to n")
"""x=int(input("Enter the number: "))
total=0
for x in range(x+1):
    total=total+x
print("Total is: ",total)"""

print("\n10:")
print("Find factorial of a number")
"""x=int(input("Enter the number: "))
fact=1
for x in range(1,x+1):
    fact=fact*x
print("Factorial is: ",fact)

print("\n11:")"""

var=10
for i in range(10):
    for j in range(2,10,1):
        if(var%2==0):
            #print(var)
            continue
        else:
            var+=1
print(var)

print("************************")
for num in range(10,14):
    for i in range(2,num):
        if(num%i)==1:
            print(num)
            #break#1213
        #break#1113
    #break#1010


    

