from datetime import datetime
import uuid
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
        
    def transfer(self, amt:int, wll:'User'):
        wll.wallet.deposit(amt)
        self.withdraw(amt)

        self.transactions.append(Transaction(reciever=wll.name,sender=self.user.name, amount=amt, types='Withdraw'))
        wll.wallet.transactions.append(Transaction(reciever=wll.name,sender=self.user.name, amount=amt, types='Deposit'))
        

class User:
    def __init__(self, name, password, balance=100):
        self.name=name
        self.unique_id = uuid.uuid4()
        self.wallet=Wallet(balance, user=self)
        self.password=password
    
    def getId(self):
        return self.unique_id

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

    def adduser(self, user:'User'):
        self.users[user.unique_id]=user

    def finduser(self, id):
        if id in self.users:
            print('User found')
            return True
        else:
            print('User not found')
            return False
        
    def register(self, name, password):
        user=User(name=name,password=password)
        self.adduser(user=user)

    def login(self, unique_id):
        if self.finduser(unique_id):
            print('logged in')
        else:
            print('login unsuccessful')
            return False

