print('Please enter the following information: ')
print()
#ID information
first= input ("First Name: ")
Last= input('Last Name: ')
email_address= input ('Email Address: ')
phone_number= input ('Phone Number: ')
job_title= input('Job Title: ')
id_number= input('ID Number: ')

#ID print 
print()
print('The ID Card Is:')
print("-----------------------------------------------------")
print()
print(f"{first.upper()}, {Last.capitalize()}")
print(f"{job_title.title()}") 
print("ID:", id_number)
#ID contact info
print(f"{email_address} ")
# +591 is just the code for Bolivia
print(f"+591 {phone_number}" )
print("-----------------------------------------------------")


