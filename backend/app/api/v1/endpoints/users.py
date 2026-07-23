from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session


from app.api.deps import get_db
from app.schemas import user
from app.crud.crud_user import create_user, authenticate_user


router = APIRouter(prefix="/users", tags=["user"])

@router.post("/signup",  status_code=status.HTTP_201_CREATED)
def signup(data: user.UserModel, db: Session = Depends(get_db)):
    
    new_user = create_user(data=data, db=db)
    return new_user

@router.post("/login", status_code=status.HTTP_200_OK, response_model=user.LoginResponse)
def login(
    data: user.LoginModel, 
    response: Response, 
    db: Session = Depends(get_db)
):
    user = authenticate_user(data, db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    response.set_cookie(
        key="session_token",
        value=str(user.user_id),
        httponly=True,
        max_age=1800,
        samesite="lax",
        secure=False 
    )

    return {
        "msg": "Logged in successfully",
        "data":{
            "name": user.name,
            "email": user.email,
            "bio": user.bio
        }
    }