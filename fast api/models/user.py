from datetime import datetime
import uuid
import json
from models.wallet import Wallet
class User:
    def __init__(self, name, password, balance=0, unique_id=None, ids=None):
        self.name=name
        if unique_id==None:
            self.unique_id = str(uuid.uuid4())[:20]
        else:
            self.unique_id=unique_id
        self.wallet=Wallet(balance, user=self, ids=ids)
        self.password=str(password)
    
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