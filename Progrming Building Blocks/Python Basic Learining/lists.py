friends=[]

new_friend= input('Type the name of a friend: ')
while new_friend!= "end":
    friends.append(new_friend)
    new_friend= input('Type the name of a friend: ')
    
    if new_friend== "end": 
        print("your friends are")
        for friend in friends:
            print(friend)

    


  

