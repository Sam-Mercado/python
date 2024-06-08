#numbers
first = int(input("1) Insert a number: "))
second = int(input("2) Insert a number: "))

if first == second:
    print("The numbers are equal")
elif first >= second:
    print (f'{first } is the greater than {second}' )

else:
    print ( f'{second}is greater than {first}')


#favorite animal 
animal= input('What is your favorite animal? ')

if animal.lower()== "rat":
    print('That is my favorite too')
else:
    print('That animal is pure crap bro')