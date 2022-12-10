#The upper() method returns the string in upper case:

x='hello,WORLD'
print(x.upper())

#lower case
y='MY WORLD'
print (y.lower())

#Remove Whitespace
#Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

#The strip() method removes any whitespace from the beginning or the end:

a = "     Hello, World!     "
print(a.strip()) # returns "Hello, World!"

#The replace() method replaces a string with another string:

a =   "Hello, World!"
print(a.replace("H", "J"))

#Split String
#The split() method returns a list where the text between the specified separator becomes the list items.

x="World,Hello"
print(x.split(","))

