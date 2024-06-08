items=[]


print('')
item_added= []
while item_added != 'quit': 
    item_added= input('Please enter the items of the shopping list (type: quit to finish):')
    items.append(item_added)
print('')
if item_added == 'quit':
    for item in items: 
       print(f'Item: {item}')
      
    for i in range(len(items)): 
        item= items[i]
        print(f'{i}.{item}')
        items.pop()

index= int(input('\n What item would you like to change? '))
new_item= input('Which item would you like to change? ')
items[index]=new_item