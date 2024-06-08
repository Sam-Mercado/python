names_bank_account=['']
account_balance=['']

while names_bank_account != 'quit':
    ban_added= input('What is the name of this account? ')
    account_balance_added= float(input('What is the balance?'))
    names_bank_account.append(ban_added)
    account_balance.append(account_balance_added)
    
if names_bank_account == "quit":
    for i in range(len(names_bank_account)): 
        name= names_bank_account[i]
        balance= account_balance[i]
        names_bank_account.pop()
        print(f'\n {i+1}:{name} - ${balance}')

        total= 0
        for i in total:
            total+=i
            print(f'\n Total: {total}')



