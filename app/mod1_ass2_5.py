import json

# Open and load the file structure
#with open("details.json", "r") as file:
#    data = json.load(file)
with open("users.json", "r") as file:
    data = json.load(file)
users={
    'aba': 100,
    'kelly':30,
    'amina':500
}
hist='Transaction history\n'
histlist=[]
name_val=input('Please enter your username: ').lower().strip()
keys=users.keys()
if name_val in keys:
    print('Successful login')
    options={1:'Check Balance', 2:'Deposit', 3:'Withdraw',4:'Transfer Money', 5:'Exit'}
    print('==== Wallet ====\n 1. Check Balance\n 2. Deposit\n 3. Withdraw\n 4. Transfer Money\n 5. Exit ')
    try:
        ans=int(input('PLease Enter your choice: '))
        if ans not in options.keys():
            print('not possible')
        else:
            while ans!=5:
                users[name_val]=users[name_val]
                if ans==1:
                    print(f"Current balance: {users[name_val]}")
                elif ans==2:
                    try:
                        new_amt=int(input('Please enter what you would like to deposit: '))
                        if new_amt<=0:
                            print('invalid deposit')
                        else:
                            users[name_val]+=new_amt
                            print( 'New balance is: ',users[name_val])
                            hist+=f"Deposited {new_amt}\n"
                            histlist.append(f"Deposited {new_amt}")
                    except ValueError:
                        print('not valid,please retry')

                elif ans==3:
                    try:
                        new_amt=int(input('Please enter what you would like to withdraw: '))
                        if new_amt<=0:
                            print('invalid withdrawal amount')
                        elif new_amt>users[name_val]:
                            print('amount too large')
                        else:
                            users[name_val]-=new_amt
                            hist += f"Withdrew {new_amt}\n"
                            histlist.append(f"Withdrew {new_amt}")
                            print( 'New balance is: ',users[name_val])
                    except ValueError:
                        print('not an integer, please retry')
                
                elif ans==4:
                    #ass3
                    reciever=input('please enter who you would like to send it to: ').lower().strip()
                    if reciever in keys:
                        try:
                            new_amt=int(input('Please enter what you would like to send: '))
                            if new_amt<=0:
                                print('invalid withdrawal amount')
                            elif new_amt>users[name_val]:
                                print('amount too large')
                            else:
                                users[name_val]-=new_amt
                                users[reciever]+=new_amt
                                hist+=f"Transferred {new_amt} to {reciever}\n"
                                print('Successfully transferred ',new_amt, 'to '+ reciever)
                                histlist.append(f"Transferred {new_amt} to {reciever}")
                                if reciever not in data:
                                    data[reciever] = {
                                        "balance": users[reciever],
                                        "history": []
                                    }
                                data[reciever]['balance']= users[reciever],
                                data[reciever].setdefault('history',[]).append(f"Recieved {new_amt} from {name_val}")
                                print( 'New balance is: ',users[name_val])
                        except ValueError:
                            print('not an integer,please retry')
                    else:
                        print('Reciever does not exist, please try again')
                print('==== Wallet ====\n 1. Check Balance\n 2. Deposit\n 3. Withdraw\n 4. Transfer Money\n 5. Exit ')
                try:
                    ans=int(input('PLease Enter your choice: '))
                    if ans not in options.keys():
                        print('not part of the options')
                except:
                    print('Make sure it is a number like 1,2,3 or 4')
            print('Thank you')
            print(hist)
            if name_val not in data:
                data[name_val] = {
                    "balance": users[name_val],
                    "history": []
                }
            data[name_val]['balance']= users[name_val],
            data[name_val].setdefault('history',[]).extend(histlist)
            with open("users.json", "w") as file:
                json.dump(data, file, indent=4)
    except ValueError:
        print('Make sure it is a number like 1,2,3 or 4')

else:
    print('Not successful please try again later')