#game based on desitions you have to take. /


choice1 = input ('You have to go to church, you are super tired and would like to still on your bed, Do you choose to STAY on your bed or get READY? ')
if choice1.lower() == 'ready': 
   print('you chose get ready, so you get up and iron a shit, buton your shirt on and now you have to choose some pants. ') 
   choice2 = input('You have two optiond GREY or BLACK: ') 
   if choice2.lower() == 'black':
       print ('Those black pants look amazing, but now you gotta get a tie that matches those pants, You can conbine those pant with pretty much any tie ') 
   elif choice2.lower() == 'grey':
       print(f'oops those are broken, you better get the black ones' )
   else:
      print( 'Incorrect choice. ')
 
elif  choice1.lower() == 'stay':
     print('you chose stay on your bed and still sleeping') 
     choice3 = input (' you get a call from your friend and she asks if you are going to go to church, do you GO or STAY?  ')
     if choice3.lower() == 'stay': 
        print('you have the best sleep in your life')
     elif choice3.lower() == 'go': 
        print('You get ready and drive to chuch, while you are sittin next to your friend you notice yuor grey pants are broken')
     else: 
        print('Incorect choice')

else: 
    print("Incorrect choice")