secret= "church"
wrong_guesses= 0

print('***********Welcome to the word guessing game!***********')
print("")
guess= str(input('What is your guess? '))
print('')

while guess!= secret: 
    print('your guress was not correct, try again.')
    print('')
    guess= str(input('What is your guess? '))
    wrong_guesses += 1

    if guess == secret:
        print ('You guessed it!')
        wrong_guesses += 1
        print(f'It took you {wrong_guesses} guesses. ')

