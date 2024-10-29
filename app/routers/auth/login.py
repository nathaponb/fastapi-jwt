from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_header_token 
from app.utils import jwt

from pydantic import BaseModel

class Login(BaseModel):
    username: str
    password: str

router = APIRouter(
    prefix="/login",
    tags=["login"],
    responses={404: {"description": "Not found"}}
)

@router.post("/")
async def login(credentials: Login):
    # Check credentials
    if credentials.username == "nathaponb" and credentials.password == "12345a":
        # Generate JWT token
        token = jwt.create_jwt_token({"sub": credentials.username})
        # return token
        return {"message": "success", "token": token}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    