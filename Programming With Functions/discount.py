import datetime
from datetime import datetime

def day_of_the_week():
    if week == 0:
        print("Monday") 
    elif week == 1: 
        print("Tuesday")
    elif week == 2: 
        print("Wednesday")
    elif week == 3:
        print("Thrusday")
    elif week == 4:
        print("Friday")
    elif week == 5:
        print("Saturday")
    else: 
        print("Sunday")

    
t=datetime.now(None)
week= t.weekday()

day_of_the_week()

get_subtotal= input('Please enter the subtotal: ')
subtotal= float(get_subtotal)
ten_per_discount = subtotal / 10
tax= round((6/100) * subtotal ,2)
total= float()
if subtotal == 0 :
    print("Thank you for your purchase")

elif week == 1  and subtotal >= 50:
    total= subtotal - ten_per_discount  + tax
    print("Sales tax amount: " + str(tax))
    print(round(total,2))

elif week == 3 and subtotal >= 50:
    total= subtotal - ten_per_discount  + tax
    print("Sales tax amount: " + str(tax))
    print(round(total,2))
    
else:
    total = subtotal + tax
    print("Sales tax amount: "+ str(tax))
    print(round(total,2))
    
get_subtotal= input('Please enter the subtotal: ')
    
    



