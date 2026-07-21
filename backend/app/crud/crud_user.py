from fastapi import APIRouter
from app.schemas.user import User_model

router = APIRouter(prefix="/users")

@router.post("/login")
async def user_login(user_data: User_model):
    try:
        pass
    except:
        pass