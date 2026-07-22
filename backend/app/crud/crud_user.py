from fastapi import status, Depends, HTTPException
from sqlalchemy.orm import Session
import traceback


from app.schemas import user
from app.api.deps import get_db
from app.models.user import User

def create_user(data: user.LoginModel, db: Session = Depends(get_db)):
    
    user = User(**data.model_dump())

    try:

        db.add(user)
        db.commit()
        return user
    
    except:

        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def authenticate_user(data: user.UserModel, db: Session) -> User | None:
    try:
        user = (
            db.query(User)
            .filter(User.email == data.email, User.name == data.name)
            .first()
        )
        
        if not user:
            return None

        if user.password != data.password:
            return None

        return user

    except Exception:
        traceback.print_exc()
        return None