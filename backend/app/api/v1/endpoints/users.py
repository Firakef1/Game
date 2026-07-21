from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session


from app.api.deps import get_db
from app.schemas import user
from app.crud.crud_user import create_user


router = APIRouter(prefix="/users")

@router.post("/signup",  status_code=status.HTTP_201_CREATED)
def signup(data: user.User_model, db: Session = Depends(get_db)):
    
    new_user = create_user(data=data, db=db)
    return new_user