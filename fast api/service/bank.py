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
        self.sample=User('Sample',' ',unique_id='0000',ids='0000')
        self.curr=self.sample


    def finduser(self, name):
        name=name.strip().lower()
        rows=database.search(name)
        if rows==None:
            print('User not found')
            return False
        else:
                print('User found')
                user=User(name=rows[1],password=rows[2],unique_id=rows[0],ids=rows[3], balance=rows[4])
                return user
            
        
    def register(self, name, password):
        if database.search(name)!=None:
            print('User already exists')
            return False
        user=User(name=name,password=password)
        database.register(name, userid=user.getId(),ids=user.wallet.getid(),balance=user.wallet.check_bal(), password=password)
        self.curr=user
        print("Successful")
        return True



    def login(self, name, password):
        rows=self.finduser(name)
        if rows != None and rows != False:
                if password==rows.password:
                    self.curr=rows
                    print('logged in')
                    return True
                
                print('login unsuccessful:Wrong password')
                return False
        print('login unsuccessful:Username not found')
        return False
    
    def transfer(self,name, amt:int):
        if self.curr is None:
            print("login first")
            return False

        receiver = self.finduser(name)
        if receiver == self.curr.name:
            print("Cannot transfer to yourself.")
            return False
        if not receiver:
            return False

        self.curr.wallet.transferin(amt, receiver)

    def logout(self):
        if self.curr==self.sample:
                print("login first")
                return False
        self.curr=User('Sample',' ',unique_id='0000',ids='0000')
        print("Logged out.")
        return True
    
   