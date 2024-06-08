
def main():
#Read the contents of the file into a list where each 
#line of text in the file is stored in a separate element in the list
    text= open_txt_file("provinces.txt")
    #print the entire list 
    print('Original list:')
    print (text)
    print
    print("------------------------------------------------------------")
    print("")
    #delet the first element using the pop() function
    print('Delete the first element list:')
    print (pop_first(text))
    print
    print("------------------------------------------------------------")

    print('Delete the last element list:')
    print (pop_last(text))
    print
    print("------------------------------------------------------------")

    for i in range(len(text)):
        if text[i] == "AB":
            text[i] = "Alberta"
    #print(provinces_list)

    # Call the list.count method which will count the
    # number of times that Alberta appears in the list.
    count = text.count("Alberta")

    print()
    print(f"Alberta occurs {count} times in the modified list.")
#Text file reader
def open_txt_file(filename):

    # Create an empty list that will store
    # the lines of text from the text file.
    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:
            
            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()
            

            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)
            #text_list.append(line) if you only display this line text is going to come out with a bunch of sings 

    # Return the list that contains the lines of text.
    return text_list

def pop_first(listname):
    pop_first = listname.pop(0)
    return listname

def pop_last(listname):
    pop_last = listname.pop()
    return listname


if __name__ == "__main__":
     main()

