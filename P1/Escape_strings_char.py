#Escape Character
#To insert characters that are illegal in a string, use an escape character.

#An escape character is a backslash \ followed by the character you want to insert.

#An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

#Example 1 -You will get an error if you use double quotes inside a string that is surrounded by double quotes:
#txt = "We are the so-called "Vikings" from the north."
#print(txt)

#To fix this problem, use the escape character \":
txt="We are the so-called \"Vikings\" from the north."
print(txt)

#Single Quote - \'
txt = 'It\'s alright.'
print(txt)

#Backslash - \\

txt = "This will insert one \\ (backslash)."
print(txt)

#\n for a new line
txt = "Hello\nWorld!"
print(txt)

# Carriage Return /r -  It means that the cursor should go back to the beginning of the line

txt = "Hell\roMinal!"
print(txt)

# Tab , \t - Puts space
txt = 'Hello\t\tWorld'
print(txt)



