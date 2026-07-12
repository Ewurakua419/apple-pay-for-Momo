options={1:'Check Balance', 2:'Deposit', 3:'Withdraw', 4:'Exit'}
bal=100
print('==== Wallet ====\n 1. Check Balance\n 2. Deposit\n 3. Withdraw\n 4. Exit ')
try:
    ans=int(input('PLease Enter your choice: '))
    if ans not in [1,2,3,4]:
        print('not possible')
    else:
        while ans!=4:
            if ans==1:
                print(bal)
            elif ans==2:
                try:
                    new_amt=int(input('Please enter what you would like to deposit: '))
                    if new_amt<=0:
                        print('invalid deposit')
                    else:
                        bal+=new_amt
                        print( 'New balance is: ',bal)
                except:
                    print('not valid,please retry')

            elif ans==3:
                try:
                    new_amt=int(input('Please enter what you would like to withdraw: '))
                    if new_amt<=0:
                        print('invalid withdrawal amount')
                    elif new_amt>bal:
                        print('amount too large')
                    else:
                        bal-=new_amt
                        print( 'New balance is: ',bal)
                except:
                    print('not valid,please retry')
            print('==== Wallet ====\n 1. Check Balance\n 2. Deposit\n 3. Withdraw\n 4. Exit ')
            try:
                ans=int(input('PLease Enter your choice: '))
                if ans not in [1,2,3,4]:
                    print('not possible')
            except:
                print('Make sure it is a number like 1,2,3 or 4')
        print('Thank you')

except:
    print('Make sure it is a number like 1,2,3 or 4')
