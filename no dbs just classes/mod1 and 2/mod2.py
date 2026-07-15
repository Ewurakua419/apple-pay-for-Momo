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
        self.hist.append(statement)
        

    def gethist(self):
        return self.hist
    
    def deposit(self, amt: int, sender='cash')->int:
        if amt<=0:
            print('invalid deposit')
            return self.balance
        self.balance+=amt
        histlist=f"Deposited {amt}"
        self.transactions.append(Transaction(reciever=self.user.name, sender=sender, amount=amt, types='Deposit'))
        self.history(histlist)
        return self.balance

    def withdraw(self, amt:int, reciever='cash')->int:
        if amt<=0:
            print('invalid withdrawal amount')
            return self.balance
        elif amt>self.balance:
            print('amount too large')
            return self.balance
        else:
            self.balance-=amt
            histlist=f"Withdrew {amt}"
            
            self.transactions.append(Transaction(reciever=reciever, sender=self.user.name, amount=amt, types='Withdraw'))
            self.history(histlist)
            return self.balance
        
    def transferin(self, amt:int, reciever:'User'):
        if amt <= self.balance:
            self.withdraw(amt,reciever=reciever.name)
            reciever.wallet.deposit(amt,sender=self.user.name)

        #self.transactions.append(Transaction(reciever=reciever.name,sender=self.user.name, amount=amt, types='Withdraw'))
        #reciever.wallet.transactions.append(Transaction(reciever=reciever.name,sender=self.user.name, amount=amt, types='Deposit'))
        

class User:
    def __init__(self, name, password, balance=100):
        self.name=name
        self.unique_id = uuid.uuid4()
        self.wallet=Wallet(balance, user=self)
        self.password=password
    
    def getId(self):
        return self.unique_id
    
    def to_dict(self):
        return {
            "id": str(self.unique_id),
            "name": self.name,
            "password": self.password,
            "balance": self.wallet.balance,
            "transaction":[transaction.to_dict()
                for transaction in self.wallet.transactions]
        }
    
class Transaction:
    def __init__(self,amount, types, sender='cash', reciever='cash'):
        
        self.sender=sender
        self.reciever=reciever
        self.amount=amount
        self.timestamp=datetime.now()
        self.type=types
    
    def to_dict(self):
        return {
            "sender": self.sender,
            "receiver": self.reciever,
            "amount": self.amount,
            "timestamp": self.timestamp.isoformat(),
            "type": self.type
        }






        

