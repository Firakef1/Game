from fastapi import status, Depends, HTTPException
from sqlalchemy.orm import Session


from app.schemas import user
from app.api.deps import get_db
from app.models.user import User

def create_user(data: user.User_model, db: Session = Depends(get_db)):
    
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