from datetime import datetime
import uuid
import json
class Transaction:
    def __init__(self,amount, types, sender='cash', reciever='cash'):
        self.id=str(uuid.uuid4())
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