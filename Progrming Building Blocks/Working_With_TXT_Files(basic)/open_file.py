
with open("books.txt") as books:
    
    for line in books: 
        book = line.strip()
        print(book)

