from fastapi import APIRouter
from starlette.requests import Request

api_rt = APIRouter()


@api_rt.get("/users")
async def profile(request: Request):
    return {"msg": "This is a Response from the server"}
