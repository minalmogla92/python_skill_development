a='I am on a vacation'
b='I am planning a vacation to Goa'

sum1= len(a)
sum2= len(b)

if(('vacation' in a) and ('vacation' in b)):
    print("Yes,'vacation' is present in a and b")
    print (sum1+sum2)
else:
    print ("nothing")