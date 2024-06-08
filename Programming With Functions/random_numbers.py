import random
 
def main():
     numbers = [16.2, 75.1, 52.3]
     words = ["Spanish", "French", "English", "Italian", "British", "Portuguese"]
 
     print(f'NUMBERS:{numbers}')
 
     numbers= append_random_numbers(numbers)
     print(f'NUMBERS:{numbers}')
 
 
     numbers= append_random_numbers(numbers, 3)
     print(f'NUMBERS:{numbers}')

     #print words 
     print(f'words: {words}')


     append_random_words(words)
     print(f'words: {words}')
     
     append_random_words(words, 3)
     print(f'words: {words}')
 
def append_random_numbers(numbers_list, quantity=1):
     for number in range(quantity):
          random_number= round(random.uniform(1,50), 1)
          numbers_list.append(random_number)
     return numbers_list
 
def append_random_words(words_list, quantity=1):
     palabras = ["apple", "smile", "plane", "TV", "sleep"]
     for word in range(quantity):
          random_word = random.choice(palabras)
          words_list.append(random_word)
     return words_list
 
main()