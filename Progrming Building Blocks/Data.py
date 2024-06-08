with open("life-expectancy.csv") as file:
    next(file)

    #list from files
    entities = []
    years = []
    life_expect = []

    #variables
    index = 0
    user_entities = []
    user_years = []
    user_life_expect = []

    #Max and min 
    highest_life_entity = ""
    highest_life = 0
    highest_year = 0


    lowest_life_entity = ""
    lowest_life = 9999
    lowest_year = 9999

    
    for line in file:
        line_stripped = line.strip()
        line_splited = line_stripped.split(",")
        
        entities.append(line_splited[0])
        years.append(int(line_splited[2]))
        life_expect.append(float(line_splited[3]))

    #life expecties
    for i in range(len(entities)):
        
        entity = entities[i]
        max_life = life_expect[i]
        min_life = life_expect[i]
        year = years[i]
           #hiest
        if max_life > highest_life: 
            highest_life = max_life
            highest_life_entity = entity
            highest_year = year
           #lowest
        elif min_life < lowest_life: 
            lowest_life = min_life
            lowest_life_entity = entity
            lowest_year = year
    
    
    print("OVERALL INFO:")
    print(f"The overall max life expectancy is: {highest_life:.2f} from {highest_life_entity} in {highest_year}")
    print(f"The overall min life expectancy is: {lowest_life:.2f} from {lowest_life_entity} in {lowest_year}")

    #variables
    highest_life_entity = ""
    highest_life = 0
    highest_year = 0

    lowest_life_entity = ""
    lowest_life = 9999
    lowest_year = 9999

    #user year
    user_input = int(input("\nEnter the year of interest: "))
    
    for i in years: 
        if i == user_input:

            user_entities.append(entities[index])
            user_years.append(int(years[index]))
            user_life_expect.append(float(life_expect[index]))
        
        index += 1

    for i in range(len(user_life_expect)):
        
        entity = user_entities[i]
        max_life, min_life = user_life_expect[i], user_life_expect[i]
        #higest
        if max_life > highest_life: 
            highest_life = max_life
            highest_life_entity = entity

        #lowest
        if min_life < lowest_life: 
            lowest_life = min_life
            lowest_life_entity = entity

        
    avarage = sum(user_life_expect) / len(user_life_expect)
    print(f"---IN {user_input} INFO:---")
    print(f"The avarage life expectancy across all countries was {avarage:.2f}")
    print(f"The max life expectancy was in {highest_life_entity} with {highest_life:.2f}")
    print(f"The min life expectancy was in {lowest_life_entity} with {lowest_life:.2f}")

    #variables
    index = 0
    user_entities = []
    user_years = []
    user_life_expect = []

    highest_life_entity = ""
    highest_life = 0
    highest_year = 0

    lowest_life_entity = ""
    lowest_life = 9999
    lowest_year = 9999  

    #country
    user_input = input("\nEnter the country of interest: ")
    
    for i in entities: 

        if i == user_input.title():

            user_entities.append(entities[index])
            user_years.append(int(years[index]))
            user_life_expect.append(float(life_expect[index]))
        
        index += 1

    for i in range(len(user_life_expect)):
        
        entity = user_entities[i]
        max_life, min_life = user_life_expect[i], user_life_expect[i]
        #higest
        if max_life > highest_life: 
            highest_life = max_life
            highest_life_entity = entity

        #lowest
        if min_life < lowest_life: 
            lowest_life = min_life
            lowest_life_entity = entity


    avarage = sum(user_life_expect) / len(user_life_expect)     
    print(f"---IN {user_input.upper()} OVERALL INFO:---")
    print(f"The overall life expectancy is {avarage:.2f}")
    print(f"The max life expectancy was in {highest_life_entity} with {highest_life:.2f}")
    print(f"The min life expectancy was in {lowest_life_entity} with {lowest_life:.2f}")