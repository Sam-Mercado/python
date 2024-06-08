#team09 
#grade Calculator 
#Samuel Mercado 

porcentage = int( input("What is your grade porsentage? ")) 

#A
if porcentage >= 97: 
    print('You got an A+')
elif porcentage >= 93: 
    print('You got an A')
elif porcentage >= 90: 
    print('You got an A-')

#B
elif porcentage >= 87 :
    print('you got a B+')
elif porcentage >= 83 :
    print('you got a B')
elif porcentage >= 80 :
    print('you got a B-')

#C
elif porcentage >= 77 : 
     print('you got a C+')
elif porcentage >= 73 : 
     print('you got a C')
elif porcentage >= 70 : 
     print('you got a C-')

#D
elif porcentage>= 60:
    print('You got a D+')
elif porcentage>= 60:
    print('You got a D')
elif porcentage>= 60:
    print('You got a D-')
else: 
    print('You got a F, sorry dude')