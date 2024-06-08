import random 
def main():
    #tenses=["past", "present", "future"]
    #numbers= ["1", "2" ]
    #tense = random.choice(tenses)
    #quantity = random.choice(numbers)

    tenses= input("choose thense: ")
    tense= tenses.lower()
    quantity= input("Choose a quantity single/plural: ")
    quantity = quantity.lower()

    make_sentence(quantity, tense)
    print()
    main()



def get_determiner(quantity):
    if quantity == 'single':
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

#Return a randomly chosen noun plural and singular
def get_noun(quantity):

    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else: 
        nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

        #randomly choose a word and return determiner 

    noun = random.choice(nouns)
    return noun
    


#Return a randomly chosen verb past, presetn and future
def get_verb(quantity, tense):
    if tense == "past": 
        verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
        

    elif tense == "present" and quantity == "single":
        verbs = [ "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"] 
        
    
    else: 
        verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    #returning randomly chosen verb
    verb = random.choice(verbs)
    return verb


def make_sentence(quantity,tense):

    word = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity,tense)

    print(f'{word.capitalize()} {noun} {verb}')




main()