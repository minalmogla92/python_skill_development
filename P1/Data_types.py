#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview
#None Type:	NoneType
from ctypes import c_int, addressof
x=5.9
print (x)
print(type(x))
#range
x=range(6)
print(x)
#list
x = ["apple", "banana", "cherry"]
print(x)
#tuple
x=("apple","banana","grape")
print(x)

#dict
x={"name":"Minal","age:":"16"}
print(x)

#set - output will have different order than what is entered
x={"apple","google","twitter"}
print(x)

#frozen set - mix of set and tuple
x=frozenset({"apple","google","mac"})
print(x)

# printing memory address

frozer_set = set(("apple", "banana", "cherry"))

#display x:
print("MEMORY ADDDESS OF FROZEN SET:---->" +str(hex(id(frozer_set))))

#display the data type of x:
print(type(x))

