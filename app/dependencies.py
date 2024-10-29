from typing import Annotated

from fastapi import Header, HTTPException
from .utils import jwt

async def get_header_token(authorization: Annotated[str, Header()]):
    # Check if the authorization header exist and starts with bearer
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=400, detail="Invalid or missing Authorization header")
    
    # Extract the token from the header
    token = authorization.split(" ")[1]

    # Verify token
    try:
        payload = jwt.decode_jwt_token(token)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
    return payload