#first rider 

first_age= int(input('What is the age of the first rider? '))
first_height= int(input('What is the height of the first rider( inches )? '))

if first_age>= 18 and first_height>= 36 : 
    secon_rider=input('Is there a second rider (yes/no)?')
if first_age<= 18 and first_height<= 36 :  
    print('Sorry, you may not ride.')

#second Rider
print(' ')
if secon_rider.lower() == "yes" : 
    secon_age= int(input('What is the age of the second rider?'))
    second_height=int (input('What is the height of the second rider?'))

if secon_age >= 18 and second_height >= 36: 
    print("Welcome to the ride. Please be safe and have fun!")
else: 
    print('Sorry, you may not ride.')
    
