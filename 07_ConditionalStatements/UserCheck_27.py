userName=input("Enter your user name: ")
password=input("Enter your password: ")
role=input("Enter your role: ")
if(userName=="YarlIt" and password=="YIT123"):
    if(role=="admin"):
        print("Welcome to admin dashboard")
    elif(role=="user"):
        print("Welcome to user dashboard")
    else:
        print("Invalid user role")
else:
    print("Invalid login credentials")

