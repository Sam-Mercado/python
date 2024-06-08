from collections import OrderedDict

def main():
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")

        #reverce list
        
        fruit_list.reverse()
        print(f"reversed: {fruit_list }")

        #append orange
        fruit_list.append("orange")
        print(f"append: {fruit_list}")

        #insert
        index= fruit_list.index("apple")
        print(fruit_list.insert(index, "cherry"))
        print(f'insert/index: {fruit_list}')

        #remove
        fruit_list.remove("banana")
        print(f'remove: {fruit_list}')

        #pop
        fruit_list.pop()
        print(f'pop: {fruit_list}')

        #sort
        fruit_list.sort()
        print(f'sort: {fruit_list}')

        #clean
        fruit_list.clear()
        print(f'clean: {fruit_list}')





if __name__=="__main__":
        main()