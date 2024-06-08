#Meal price calculator.
#Samuel Mercado - Team09

from pickletools import float8

#prices
Child= float(input("What is the price of a child's meal? ") ) 
adult= float(input("What is the price of an adult's meal? ") )

#number of...
num_Childr= int( input("How many children are there? "))
num_adults= int( input("How many adults are there? "))
#Taxes
tax= float(input('What is the sales tax rate?'))


#math
to_pay= (num_Childr * Child) + (num_adults * adult)
sales_tax=(to_pay * tax)/ 100
total= to_pay + sales_tax

#results 
print('subtotal: ',to_pay) 
print('Sales Tax: ',sales_tax )
print('Total:', total)

#payment
payment=float( input('What is the payment amount?'))
change= payment - total
print(f'change:{change:.2f} ')

 

