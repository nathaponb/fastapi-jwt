from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_header_token 

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_header_token)],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def get_users(payload: dict = Depends(get_header_token)):
    return [{"id": 1, "name": "nathaponb", "payload": payload}]