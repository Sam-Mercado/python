import random 

words_list= ["summer","winter","moroni","mormon"]

#start game 
print('**********WELCOME WORDLE GAME**********')
print('')
word= random.choice(words_list)
board = []
blanks=len(word)
guess=[]


print(word)
print(f'Guess the word:', "_ "*blanks)
guess= input('What is you guess? ')

while guess != word: 
  for i in range(len(word)):
    if word[i] in correct_letter:
      guess1 = guess[:i] + word[i] + guess[i+1:]
      print(guess1)
      guess= input('\nWhat is you guess? ')

  if len(guess)< len(word):
    print("Sorry, the guess must have the same number of letters as the secret word")
    guess= input('What is you guess? ')

if guess== word: 
  print('Congrats, you guessed it')


       