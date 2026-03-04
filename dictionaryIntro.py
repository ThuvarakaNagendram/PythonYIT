"""data={
    "name":"Seelan",
    "age":39,
    "gender":"male"
    }
print(data)
print(type(data))"""

d=[("name","Seelan"),("age",39),("gender","male"),("native","Puloly")]
data=dict(d)
print(data)
print(type(d))
print(type(data))
print(data["name"])
print(data.get("age"))

print(data.get("dob","2002/03/12"))#Assign default value

data["NIC"]=198742047807
print(data)

data.update({"age":40,"NIC":1987})
print(data) 

print("*********************************************")

key=data.keys()
print(key)

value=data.values()
print(value)

item=data.items()
print(item)

print("*********************************************")

for key in data.keys():
    print(key)
    #print(key,data[key])

print("*********************************************")

for value in data.values():
    print(value)

print("*********************************************")

for item in data.items():
    print(item)

print("*********************************************")

d1=data.copy()
print(d1)

print("*********************************************")

del data["name"]#delete key value
print("after applied del-name: ",data)

data.pop("age")#remove
print("after applied pop-age: ",data)

data.popitem()#remove last
print("after applied popItem",data)

#data.clear()#clear all
#print("after applied clear: ",data)

print("*********************************************")

