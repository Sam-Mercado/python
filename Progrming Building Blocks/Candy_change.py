number= int(input("Please type a positive number:"))

while number< 0:
    print("Sorry, that is not a positive number. Please try again.")
    number= int(input("Please type a negative number:"))
print(f"your number is {number}")


candy= str(input( "May I have a piece of candy?"))

while candy.lower() == "no": 
    candy=str(input( "May I have a piece of candy?"))
print("Thank you ")
    

