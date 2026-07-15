from datetime import datetime
import uuid
import json
from user import User
from transaction import Transaction
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
