from datetime import datetime
import uuid
import json
from models.wallet import Wallet
class User:
    def __init__(self, name, password, balance=0):
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