#Does the person have a job, and if so, how long have they worked there, and how much money do they make?

job_qualifycation= input("Do you have a job? ")
if job_qualifycation.lower() == "yes":
    job_time=int(input('How long have you been working there? '))
    money_made= float(input('How much money do you make per year? '))
  

if job_time >= 12 and money_made >= 45000:
        loan_reason= input('What do you want the money for? ')
        credit_score= float(input('What is your credit score? '))
        other_debt= float(input('How much other debt does the person have?'))
        persons_money=float(input('How much money does the person have??'))
else: 
    print("Couln't qualify")
    





        



