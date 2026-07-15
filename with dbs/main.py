from service.bank import Bank
bank=Bank("Ecobank")
ans=4
done=False
while ans!=00:
    while done==False:
        print('==== Wallet ====\n 1. Register\n 2. Login \n Enter 00 to exit bank\n ')
        try:
            ans=int(input('PLease Enter your choice: '))
            if ans==1:
                name=(input('PLease Enter your name: ')).strip().lower()
                passcode=(input('PLease Enter your password: '))
                done=bank.register(name=name,password=passcode)

            elif ans==2:
                name=(input('PLease Enter your name: ')).strip().lower()
                passcode=(input('PLease Enter your password: '))
                done=bank.login(name=name,password=passcode)

            else:
                print('Invalid choice')
        except ValueError:
            print('Make sure it is a number like 1,2,3 or 4')
    
    print('==== Wallet ====\n 1:Check Balance \n 2:Deposit\n 3: Withdraw\n 4:Transfer Money \n 00:Exit \n 11: Return')
    try:
        ans=int(input('PLease Enter your choice: '))
        if ans==1:
                    print(f"Current balance: {bank.curr.wallet.balance}")
        elif ans==2:
            try:
                new_amt=int(input('Please enter what you would like to deposit: '))
                bank.curr.wallet.deposit(new_amt)

            except ValueError:
                print('Make sure it is a number like 1,2,3 or 4')
        elif ans==3:
            try:
                new_amt=int(input('Please enter what you would like to withdraw: '))
                bank.curr.wallet.withdraw(new_amt)

            except ValueError:
                print('Make sure it is a number like 1,2,3 or 4')
        
        
        elif ans==4:
            try:
                reciever=str(input('Please enter who you would like to send to: ')).lower().strip()
                new_amt=int(input('Please enter what you would like to transfer: '))

                bank.transfer(name=reciever,amt=new_amt)
            except ValueError:
                print('Make sure it is a number like 1,2,3 or 4')
                 
        elif ans==11:
            done=False
        if ans == 0:
            print("Thank you for using the Wallet.")
            break
    except ValueError:
            print('Make sure it is a number like 1,2,3 or 4')


    