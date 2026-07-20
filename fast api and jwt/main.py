from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from service.bank import Bank
import database
import auth
bank=Bank("Ecobank")
app = FastAPI()
class RegisterRequest(BaseModel):
    username: str
    password: str

class DepositRequest(BaseModel):
    token: str
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
    if success is not None:
        token=auth.create_token(success)
        return {"message": "Login successful", "username": data.username, "access_token": token}

    return {"message": "Login unsuccessful"}

@app.get("/user/{username}")
def finduser(username:str):
    return bank.finduser(username)        




@app.post("/deposit")
def deposit(data: DepositRequest, ):
    payload = auth.verify_token(data.token)
    if payload is None:
        raise HTTPException(401)
    balance=bank.deposit(payload["Username"],data.amount)
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