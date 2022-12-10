x=10
y=20
z=x+y
print(z)

def sum():
    a=12
    print(z*a)


sum()

def min():
    c=15
    print(c*x)

min()

#x="mogla"
def myname():
    x = "mogla"
    print(x)
myname()


def mynames():
    print(x)

mynames()

surname=" Mogla"
def mname():
    m="minal"
    print(m+surname)

mname()

def all():
    print("My father name is Sanjeev"+surname)
    print("Suman"+surname)
all()

party="water"

def drinks ():
    whisky=" Glenfidhich"
    print(party+whisky)

drinks()


c="suits"
def series():
    print (c)

series()
c="breaking bad"
print(c)

#The global Keyword -Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

#To create a global variable inside a function, you can use the global keyword.
def myfun():
    global y
    y="sony"

myfun()
print(y)
