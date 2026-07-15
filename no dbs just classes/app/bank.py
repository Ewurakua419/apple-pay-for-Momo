from datetime import datetime
import uuid
import json
from models.user import User
from models.transaction import Transaction
import database
class Bank:
    def __init__(self):
        self.users={}
        self.curr=None

    def adduser(self, user:'User'):
        self.users[user.unique_id]=user


    def finduser(self, name):
        for item in self.users.values():
            if name==item.name:
                print('User found')
                return item
        else:
            print('User not found')
            return False
        
    def register(self, name, password):
        for item in self.users.values():
            if name==item.name:
                print('User already exists')
                return False
        user=User(name=name,password=password)
        database.register(name=name,password=password,balance=0)
        self.adduser(user=user)


    def login(self, name, password):
        for item in self.users.values():
            if name==item.name:
        
                if password==item.password:
                    self.curr=item
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
        if receiver == self.curr:
            print("Cannot transfer to yourself.")
            return False
        if not receiver:
            return False

        self.curr.wallet.transferin(amt, receiver)

    def logout(self):
        if self.curr is None:
                print("login first")
                return False
        self.close()
        self.curr=None
        print("Logged out.")
        return True
    
    def close(self):
        try:
            with open("users.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
        data['Users']=[
            user.to_dict()
            for user in self.users.values()
        ]
        with open("users.json", "w") as file:
                json.dump(data, file, indent=4)

    def open(self):
        try:
            with open("users.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data={}
        self.users={}
        for user_data in data.get("Users", []):
            user = User(
                name=user_data["name"],
                password=user_data["password"],
                balance=user_data["balance"]
            )

            user.unique_id = uuid.UUID(user_data["id"])
            for t in user_data.get("transaction", []):
                transaction = Transaction(
                    amount=t["amount"],
                    types=t["type"],
                    sender=t["sender"],
                    reciever=t["receiver"]
                )

                transaction.timestamp = datetime.fromisoformat(t["timestamp"])
                user.wallet.transactions.append(transaction)


            self.users[user.unique_id] = user

        
