# print it in one line

print("Samuel Mercado. ", end="")
print("Business Developer.")

# commitment 1
word= 'commitment' 
for letter in word: 
    print(letter)

print('')
# 1:commitment "M upper"

word= ['c','o', 'm','m','i','t','m','e','n','t']
for letter in word: 
    if letter =='m':
        print(letter.upper())
    else:   
     print(letter)
print("")
#2
word= ['c','o', 'm','m','i','t','m','e','n','t']
for letter in word: 
    if letter =='t':
        print(letter.upper(),end="")
    else:   
     print(letter, end="")

#3 
word= ['c','o', 'm','m','i','t','m','e','n','t']

favorite_letter= str(input('What is your favorite letter in "commitment"? '))
for letter in word: 
    if letter == favorite_letter.lower():
        print("_",end="")
    else:   
     print(letter, end="")









