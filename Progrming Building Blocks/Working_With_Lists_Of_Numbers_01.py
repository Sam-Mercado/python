numbers=[12,1,2,3,4,5,6,7,8,9]
total=0 

for number in numbers:
    print(number)
print('Sum:')
for number in numbers:
    total= total + number
print(f'the total is :{total}')
print('')

print('Average:')
for number in numbers:
    total= total + number 
    average=total / len(numbers)
print(average)
print('')

print("Higher number:")
high_num= numbers[0]
for number in numbers:
    if number > high_num:
        high_num= number
print(high_num)




