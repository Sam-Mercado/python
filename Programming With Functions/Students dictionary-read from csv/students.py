import csv 



def main():
    ID_NUMBER= 0 
    STUDENT_NAME = 1
    
    student_dictionary = read_dictionary( "students.csv" , ID_NUMBER)

    id_number= input("Please enter an I-Number: ")

    id_number= id_number.replace("-", "")
# Determine if the user input is formatted correctly.
    if not id_number.isdigit(): # .isdigit()is a string method that returns True 
                                #if all characters in the string are digits
        print("Invalid character in I-Number")
    else:
        if len(id_number) < 9:
            print("Invalid I-Number: too few digits")
        elif len(id_number) > 9: 
            print("Invalid I-Number: too many digits")

        else: 
            if id_number not in student_dictionary: 
                print("No such student")
            else: 
                value = student_dictionary[id_number]
                name = value[STUDENT_NAME]

                print(name)



def read_dictionary(filename, key_column_index):
    #dictionary that will store data from the csv
    dictionary= {}
        #Read the contents of a CSV file into a compound
        #dictionary and return the dictionary
    with open(filename, "rt") as csv_file:
        
        reader = csv.reader(csv_file)

        next(reader)  
        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader: 
                # From the current row, retrieve the data
                # from the column that contains the key.
                key= row_list[key_column_index]
                #Store the data from the current row
                # into the dictionary.
                dictionary[key] = row_list
                #Return: a compound dictionary that contains
            #the contents of the CSV file.
    return dictionary



if __name__ == "__main__":
    main()       
    
#------------------------------------------------------------------------
