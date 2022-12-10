#Assign sting to a variable
a='Hello'
print(a)

#Multiline sting
x='''nijjokppopo
kojokokokpp
kjojokjokpkpkpkp

knjojok'''
print(x)

#Strings are Arrays

#Python does not have a character data type, a single character is simply a string with a length of 1.

#Square brackets can be used to access elements of the string.
y='Hello World'
print(y[4])

#Looping Through a String

#Since strings are arrays, we can loop through the characters in a string, with a for loop.

for z in ('apple'):
    print(z)

#String Length
#To get the length of a string, use the len() function.

b=('google, name')
print(len(b))

#Check String
#To check if a certain phrase or character is present in a string, we can use the keyword in

c=('check if check is present or enter 1 char from this line')
print('check' in c)

#Use it in an if statement:

d=('checking if free is present')
if 'check' in d:
    print('yes,its present')
if 'free' not in d:
    print ('noo')


# Check if NOT
#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

#Check if "expensive" is NOT present in the following text:
v='check if not present'
print('true' not in v)
print('check' not in v)
