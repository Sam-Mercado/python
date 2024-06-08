import csv
from datetime import datetime

def main():
    #variables 
    STORE_NAME= "SAMUEL'S STORE"
    total= 0
    items= len([])

    try: 
        
        products_in_store = read_dictionary("products.csv" )
        print(products_in_store)
        # open request file 
        with open("request.csv", "rt") as file: 
            request= csv.reader(file)
            #skip the first line in the csv file
            next(request)
            print("")
            #name of the store, 
            print(f"---------------{STORE_NAME}--------------------")
            print("Requested Items:")
            #go thorough each row in the request csv and separate the columns as
            #product_num(column one) and quantity(column two)
            for row in request:
                #here I'm separating the row, product_num = row[0] to get to the first column
                #and quantity = row[1] to get to the second column 
                product_num = row[0]
                quantity = row[1]
                # If the product_num is in products_in_store
                if product_num in products_in_store:
                      #it will match each product_num with products_in_store 
                      #and save it as "value", then the progam gets the "name" column in products.csv
                      #as well as the "price"
                      value = products_in_store[product_num]
                      name = value[1]
                      price = value[2]
                      #the following part is appending the items
                      items.append(name)
                      total+= float(price)
            
                print(f'{name}:{quantity} @ { float(price) * float(quantity)}')
        
            tax= calculate_tax(total)
            sales_tax= tax+ float(total)
            now = datetime.now()
            formatted_now = now.strftime("%a %b %d   %H:%M:%S   %Y")

            print('')
            print(f"Number of items:{items}")
            print(f'Total Price: {total}')
            print(f'Tax Amount: {tax}')
            print(f'Sales Tax: {sales_tax}\n') 
            print(f'Thank you for shopping at {STORE_NAME}')
            print(f"Current date and time:{formatted_now}\n")

    except FileNotFoundError as e:
        print(f"Error: missing file\n{e}")
    except PermissionError as e:
        print(f"Error: permission denied for file\n{e}")
    except KeyError as e:
        print(f"Error: unknown product ID in the request.csv file\n'{e}'")

    

def read_dictionary(filename, key_column_index=0):

    dictionary={}

    with open(filename, "rt") as file: 
        reader= csv.reader(file)
        next(reader)
        for row in reader:
            #value = dictionary_name[key] to find something in the dictionary
                key = row[key_column_index]
            #     #product = product_number[key_column_index]
                dictionary[key] = row


        return dictionary
    
def calculate_tax(amount):
    tax_rate = 0.06 
    tax_amount = amount * tax_rate
    return round(tax_amount,2)
    


        
if __name__ == "__main__": 
    main()