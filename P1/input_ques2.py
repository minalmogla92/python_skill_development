
emp1= input('Enter company name')
if (  (  ('calsoft' in emp1)or('dell' in emp1)  )   and ('oracle' in emp1)):
    print('Valid employee')


else:
    x='invalid employee'
    print(x)
    print(emp1[17:])
