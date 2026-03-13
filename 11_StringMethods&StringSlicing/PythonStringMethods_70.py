s="Welcome to YarlIT"
print(len(s))
print(s)
print(s.lower())
print(s.upper())
print(s.title())
print(s.capitalize)
print(s.swapcase())


print("isalpha:",s.isalpha())
print("isdigit:",s.isdigit())
print("isLower:",s.islower())
print("isupper:",s.isupper())
print("isspace:",s.isspace())
print("_________________________")

print(s.startswith('Welcome'))
print(s.endswith('t'))
print("_________________________")

print(s.find('to'))
print(s.find('Hello'))
print("_________________________")

print(s.index('Y'))
print("_________________________")

print(s.count('t'))
print(s.replace("YarlIT","Python"))
