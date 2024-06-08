numbers=[]
higer_number= -1
smallest_num= 98989898989898989

print('Insert some positive and negative numbers and write "end" when you are done:')
user_num= input('What is you number: ')
while user_num != 'end':
    numbers.append(user_num)
    user_num= input('What is you number: ')
    if user_num == 'end':
      for number in numbers:
         print(number)
sum = 0 
for number in numbers:
    sum = sum + number
print(f'the sum is:{sum}')

average= sum / len(number)
print(f'THe average is: {average}')

for number in numbers:
    if number> higer_number:
        higer_number= number
print(f"The largest number is: {higer_number}")

for number in numbers: 
    if number>0 and number< smallest_num: 
       print(f"The smallest positive number is: {smallest_num}")

sorted_list= sorted(numbers)
print("The sorted list is:")
for number in sorted_list:
    print(number) 
    