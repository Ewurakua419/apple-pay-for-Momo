from bank import Bank
import database
bank=Bank("Ecobank")
ans=4
options={1:'Check Balance', 2:'Deposit', 3:'Withdraw',4:'Transfer Money', 0:'Exit'}
while ans!=00:
    
    print('==== Wallet ====\n 1. Register\n 2. Login \n Enter 00 to exit bank\n ')
    try:
        ans=int(input('PLease Enter your choice: '))
        if ans==1:
            name=(input('PLease Enter your name: ')).strip().lower()
            passcode=(input('PLease Enter your password: '))
            bank.register(name=name,password=passcode)

        elif ans==2:
            name=(input('PLease Enter your name: ')).strip().lower()
            passcode=(input('PLease Enter your password: '))
            

           

    
    except ValueError:
        print('Make sure it is a number like 1,2,3 or 4')
    