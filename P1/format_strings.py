#Use the f method to insert numbers into strings:


first_name="Minal "
last_name="Mogla"
cash =20
bank=19
money=22
print(f"My name is {first_name+last_name} : I have {cash+bank} ruppees")

#----------------------------

age=36
name='Minal Mogla'
print(f'My name is :{name} , My age is:{age}')

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

quantity = 3
itemno = 567
price = 49.95

print(f'I want to pay ${price} for the item {itemno} for {quantity} pieces')

##OR
quantity = 4
itemno = 999
price = 50.44
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

