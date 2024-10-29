from fastapi import Depends, FastAPI

from .dependencies import get_header_token
from .routers import users, auth
from .routers.auth import login
from .config import config

# Load RSA keys
with open("private.pem", "rb") as f:
    config.PRIVATE_KEY = f.read()

with open("public.pem", "rb") as f:
    config.PUBLIC_KEY = f.read()

app = FastAPI()

app.include_router(users.router)
app.include_router(login.router)

@app.get("/")
async def root():
    return {"message": "success"}