from datetime import datetime
import uuid
import json
from models.user import User
from models.transaction import Transaction
from typing import Optional
import database
class Bank:
    def __init__(self,name):
        self.name=name


    def finduser(self, name):
        name=name.strip().lower()
        rows=database.search(name)
        if rows==None:
            print('User not found')
            return None
        else:
                print('User found')
                user=User(name=rows[1],password=rows[2],unique_id=rows[0],ids=rows[3], balance=rows[4])
                return user
            
        
    def register(self, name, password):
        if database.search(name)!=None:
            print('User already exists')
            return None
        user=User(name=name,password=password)
        database.register(name, userid=user.getId(),ids=user.wallet.getid(),balance=user.wallet.check_bal(), password=password)
        
        print("Successful")
        return user



    def login(self, name, password):
        rows=self.finduser(name)
        if rows != None and rows != False:
                if password==rows.password:
                    return rows
                
                print('login unsuccessful:Wrong password')
                return None
        print('login unsuccessful:Username not found')
        return None
    
    def transfer(self,sender_name,reciever_name, amt:int):
        sender=self.finduser(sender_name)
        if sender is None:
            print("Sender not found")
            return None

        receiver = self.finduser(reciever_name)
        if receiver == sender:
            print ("Cannot transfer to yourself.")
            return None
        if not receiver:
            print( "Receiver not found")
            return None

        sender.wallet.transferin(amt, receiver)
        print ("Transfer successful")
        return True

    def logout(self):
        """if self.curr==self.sample:
                print("login first")
                return False
        self.curr=User('Sample',' ',unique_id='0000',ids='0000')"""
        print("Logged out.")
        return True
    
    def deposit(self, username, amount):
        user = self.finduser(username)

        if user is None:
            return None

        user.wallet.deposit(amount)
        return user.wallet.balance
    
    def withdraw(self, username, amount):
        user = self.finduser(username)

        if user is None:
            return None

        user.wallet.withdraw(amount)
        return user.wallet.balance
   