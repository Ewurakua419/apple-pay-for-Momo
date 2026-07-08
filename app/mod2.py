from datetime import datetime
import uuid
import json
class Wallet:
    def __init__(self,balance,user:'User'):
        self.balance=balance
        self.hist=[]
        self.user=user
        self.transactions=[]

    def check_bal(self)->int:
        return self.balance
    
    def history(self, statement:str):
        self.hist.extend(statement)
        

    def gethist(self):
        return self.hist
    
    def deposit(self, amt: int)->int:
        if amt<=0:
            print('invalid deposit')
            return self.balance
        self.balance+=amt
        histlist=[f"Deposited {amt}"]
        self.transactions.append(Transaction(sender='Cash',reciever=self.user.name, amount=amt, types='Deposit'))
        self.history(histlist)
        return self.balance

    def withdraw(self, amt:int)->int:
        if amt<=0:
            print('invalid withdrawal amount')
        elif amt>self.balance:
            print('amount too large')
            return self.balance
        else:
            self.balance-=amt
            histlist=f"Withdrew {amt}"
            self.transactions.append(Transaction(reciever='Cash',sender=self.user.name, amount=amt, types='Withdraw'))
            self.history(histlist)
            return self.balance
        
    def transferin(self, amt:int, reciever:'User'):
        reciever.wallet.deposit(amt)
        self.withdraw(amt)

        self.transactions.append(Transaction(reciever=reciever.name,sender=self.user.name, amount=amt, types='Withdraw'))
        reciever.wallet.transactions.append(Transaction(reciever=reciever.name,sender=self.user.name, amount=amt, types='Deposit'))
        

class User:
    def __init__(self, name, password, balance=100):
        self.name=name
        self.unique_id = uuid.uuid4()
        self.wallet=Wallet(balance, user=self)
        self.password=password
    
    def getId(self):
        return self.unique_id
    
    def upload(self):
        with open("users.json", "r") as file:
            data = json.load(file)
        if self.user.unique_id not in data:
                data[self.user.unique_id ] = {
                    "balance": self.balance,
                    "history": []
                }
        data[self.user.unique_id ]['balance']= self.wallet.balance,
        data[self.user.unique_id ].setdefault('history',[]).extend(self.wallet.transactions)
        with open("users.json", "w") as file:
                json.dump(data, file, indent=4)

class Transaction:
    def __init__(self, sender, reciever,amount, types):
        
        self.sender=sender
        self.reciever=reciever
        self.amount=amount
        self.timestamp=datetime.now()
        self.type=types

class Bank:
    def __init__(self):
        self.users={}
        self.curr=None

    def adduser(self, user:'User'):
        self.users[user.unique_id]=user

    def finduser(self, name):
        for item in self.users:
            if name==item.name:
                print('User found')
                return item.unique_id
        else:
            print('User not found')
            return False
        
    def register(self, name, password):
        for item in self.users:
            if name==item.name:
                print('User already exists')
                return False
        user=User(name=name,password=password)
        self.adduser(user=user)


    def login(self, name, password):
        for item in self.users:
            if name==item.name:
        
                if password==item.password:
                    self.curr=item
                    print('logged in')
                
                print('login unsuccessful:Wrong password')
                return False
        print('login unsuccessful:Username not found')
        return False
    
    def transfer(self,name, amt:int):
        if self.finduser(name)!=False:
            reciever=self.finduser(name)
            if self.curr==None:
                print("login first")
                return False
            self.curr.transferin(reciever=reciever,amt=amt)

    def logout(self):
        if self.curr==None:
                print("login first")
                return False
        self.curr.upload()
        self.curr=None




        

