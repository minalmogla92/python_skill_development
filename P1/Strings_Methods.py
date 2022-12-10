#capitalize() -Converts the The capitalize() method returns a string where the first character is upper case, and the rest is lower case.


txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

txt = "pYTHON IS FUN!"
x = txt.capitalize()
print (x)

txt = "36 is MY AGE."
x = txt.capitalize()
print (x)
#--------------------------------------------

#casefold() -The casefold() method returns a string where all the characters are lower case.

#This method is similar to the lower() method, but the casefold() method is stronger, more aggressive,
# meaning that it will convert more characters into lower case,
# and will find more matches when comparing two strings and both are converted using the casefold() method.

txt = "Hello, AND Welcome to Jurrasic Park"
x = txt.casefold()
print(x)

txt= "Hello, AND Welcome to Jurrasic Park"
x=txt.lower()
print(x)

mystr = 'außen'
print(mystr.casefold())

mystr = 'außen'
print(mystr.lower())

######################################################
#P  rint the word "banana", taking up the space of 20 characters, with "banana" in the middle:

txt = "banana"
x = txt.center(20)
print(x)

#string.center(length, character)

##############################################
#The count() method returns the number of times a specified value appears in the string.
txt = "I love apples, apple are my favorite fruit"
x = txt.count("a")
print(x)

#string.count(value, start, end)
txt = "I love apples, apple apple are my favorite fruit"
x = txt.count("apple", 10, 26)
print(x)

