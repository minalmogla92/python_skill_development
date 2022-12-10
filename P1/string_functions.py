Statement1 = "Californa Server Funki 192.206.34.5"
Statement2 = "Atlantic Server Pika 210.245.67.89"

# From Statement 1 and Statement2 find location Server name and server ip and location
# eg  location : california servername: funki ip_address: 192.206.34.5 ---> print the output in this format

Cali=(Statement1.split('Server'))


One=Cali[0]
two=Cali[1]

#print(two)

space=(two.split(' '))
#print(space)
funkloc =space[1]
#print(funkloc)
iploc=space[2]
#print(iploc)

#print(One ,'Servername:',funkloc,'ipaddress:',iploc)

Atlantic=(Statement2.split(' '))
#print(Atlantic)

loc_of_atlantic=Atlantic[0]
loc_of_pika=Atlantic[2]
loc_of_ip=Atlantic[3]

#print(loc_of_atlantic,'servername:',loc_of_pika,'ipaddress:',loc_of_ip)

print(Statement1.replace(iploc,"Minal&&"))

##Statement -My Name is Minal Mogla,My Address is H No 244,Chandigarh,9988061734

Line='My Name is Minal Mogla,My Address is HNo 244,Chandigarh,9988061734'

split_1=(Line.split(','))

print("************SPLI_1***************************")
print(split_1)
name_loc=split_1[0]
print("***************************************")
print(name_loc)
print("***************************************")
name_split=(name_loc.split(' '))
print("***************************************")
print(name_split)
print("***************************************")
find_firstname=name_split[3]
find_surname=name_split[4]
address=split_1[1]
print(address)
split_address=(address.split(' '))
print(split_address)
hnumber=split_address[3]
house_number=split_address[4]
city=split_1[2]
print(city)
mobile=split_1[3]




#final print
print('Name:',find_firstname , find_surname)
print(hnumber,house_number)
print('City:',city)
print('Mobile:',mobile)
