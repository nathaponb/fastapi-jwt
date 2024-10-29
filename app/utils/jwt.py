import jwt
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone

from ..config import config

class TokenData(BaseModel):
    sub: str
    exp: datetime


def create_jwt_token(data: dict) -> str:
    """Generate a JWT token with specific data"""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, config.PRIVATE_KEY, algorithm="RS256")
    return token


def decode_jwt_token(token: str) -> TokenData:
    """Decode a JWT token to verify and extract payload"""
    try:
        payload = jwt.decode(token, config.PUBLIC_KEY, algorithms="RS256")
        return TokenData(**payload)
    except jwt.ExpiredSignatureError as e:
        raise jwt.InvalidTokenError("Token has expired.") from e
    except jwt.InvalidTokenError as e:
        raise jwt.InvalidTokenError("Invalid token.") from e
    except Exception as e:
        print(e)
        raise Exception("An error occurred while decoding the token.") from e