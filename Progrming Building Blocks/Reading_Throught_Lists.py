
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = 9999
youngest_name = ""
#print(people)
for i in people: 
    data= i.split()
    name= data[0]
    age= int(data[1])

    if age < youngest_age:
        youngest_age=age
        youngest_name= name

print(f"The youngest person is: {youngest_name} with an age of {youngest_age}")
