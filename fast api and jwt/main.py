from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from service.bank import Bank
import database
import auth
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)
bank=Bank("Ecobank")
app = FastAPI()
class RegisterRequest(BaseModel):
    username: str
    password: str

class DepositRequest(BaseModel):
    amount: int

class WithdrawRequest(BaseModel):
    amount: int

class TransferRequest(BaseModel):
    receiver: str
    amount: int

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = auth.verify_token(token)

    if payload is None:
        raise HTTPException(401)

    return payload

@app.post("/register")
def register(data: RegisterRequest):
    user=bank.register(name=data.username,password=data.password)
    if user is None:# if user already exists
        raise HTTPException(
            status_code=409,
            detail="Username already exists"
        )
    token=auth.create_token(user)
    return{
        "access_token": token, 
        "token_type": "bearer"
    }

@app.post("/login")
def login(data: RegisterRequest):
    success=bank.login(name=data.username,password=data.password)
    if success is not None:
        token=auth.create_token(success)
        return {"message": "Login successful",  "access_token": token, "token_type": "bearer"}

    raise HTTPException(
    status_code=401,
    detail="Invalid credentials"
)

@app.get("/user/{username}")
def finduser(username:str):
    return bank.finduser(username)        




@app.post("/deposit")
def deposit(data: DepositRequest, payload=Depends(get_current_user)):
    if payload is None:
        raise HTTPException(401)
    balance=bank.deposit(payload["Username"],data.amount)
    return {
        "message": "Deposit successful",
        "balance": balance
    }
    
    

@app.post("/withdraw")
def withdraw(data:WithdrawRequest,payload=Depends(get_current_user)):
    if payload is None:
        raise HTTPException(401)
    balance=bank.withdraw(payload["Username"],data.amount)
    
    return{
        "message":"Withdrawal  succcessful",
        "balance":balance
    }
    
@app.post("/transfer")
def transfer(item:TransferRequest, payload=
             Depends(get_current_user)):
    if payload is None:
        raise HTTPException(401)
    bank.transfer(sender_name=payload["Username"],reciever_name=item.receiver,amt=item.amount)
    return {
        "message": "Transfer completed",
        "sender":payload["Username"],
        "recipient": item.receiver,
        "amount":item.amount
    }

@app.get("/transactions/{wallet_id}")
def gettransactions(wallet_id:str):
    return database.getTransactions(wallet_id=wallet_id)