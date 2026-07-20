from fastapi import FastAPI
from pydantic import BaseModel
from service.bank import Bank
import database
bank=Bank("Ecobank")
app = FastAPI()
class RegisterRequest(BaseModel):
    username: str
    password: str

class DepositRequest(BaseModel):
    username: str
    amount: int

class WithdrawRequest(BaseModel):
    username: str
    amount: int

class TransferRequest(BaseModel):
    sender: str
    receiver: str
    amount: int

@app.post("/register")
def register(data: RegisterRequest):
    bank.register(name=data.username,password=data.password)
    return{
        "success": True,
        "username": data.username
    }

@app.post("/login")
def login(data: RegisterRequest):
    success=bank.login(name=data.username,password=data.password)
    if success:
        
        return {"message": "Login successful", "username": data.username}

    return {"message": "Username already exists"}

@app.get("/user/{username}")
def finduser(username:str):
    return bank.finduser(username)        




@app.post("/deposit")
def deposit(data: DepositRequest):
    
    balance=bank.deposit(data.username,data.amount)
    if balance is None:
        return {"message": "User not found"}

    return {
        "message": "Deposit successful",
        "balance": balance
    }
    
    

@app.post("/withdraw")
def withdraw(amt:WithdrawRequest):
    balance=bank.withdraw(amount=amt.amount,username=amt.username)
    if balance is None:
        return {"message": "User not found"}

    return{
        "message":"Withdrawal  succcessful",
        "balance":balance
    }
    
@app.post("/transfer")
def transfer(item:TransferRequest):
    bank.transfer(sender_name=item.sender,reciever_name=item.receiver,amt=item.amount)
    return {
        "message": "Transfer completed",
        "sender":item.sender,
        "recipient": item.receiver,
        "amount":item.amount
    }

@app.get("/transactions/{wallet_id}")
def gettransactions(wallet_id:str):
    return database.getTransactions(wallet_id=wallet_id)