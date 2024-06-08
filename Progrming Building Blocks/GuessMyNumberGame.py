import random
magic_number= random.randint(1,100)
guess= int(input('What is your guess?'))
if guess == magic_number: 
        print('you guess it!')
while guess != magic_number:
    if guess> magic_number: 
        print('Lower')
        guess= int(input('What is your guess?'))
    
    elif guess< magic_number: 
        print ('Higher')
        guess= int(input('What is your guess?'))
    
    

