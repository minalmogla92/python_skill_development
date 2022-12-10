#Slicing
#You can return a range of characters by using the slice syntax.

#Specify the start index and the end index, separated by a colon, to return a part of the string.

x='helloworld'
print(x[2:6])

#Slice From the Start
y="Hello World"
print(y[:3])

#Slice To the End
#Get the characters from position 2, and all the way to the end:
z="Hello World"
print(z[2:])

#Negative Indexing
#Use negative indexes to start the slice from the end of the string:
#Get the characters:
#From: "o" in "World!" (position -4)

#To, but not included: "d" in "World" (position -1):

a='Hello World'
print(a[-4:-1])
