from fastapi import status, Depends, HTTPException
from sqlalchemy.orm import Session
# import traceback


from app.schemas import user
from app.api.deps import get_db
from app.models.user import User
from app.core import security

def create_user(data: user.UserModel, db: Session = Depends(get_db)):


    user_data = data.model_dump(exclude={"password"})
    hashed_password = security.generate_hash(data.password)
    user = User(**user_data, password=hashed_password)


    try:

        db.add(user)
        db.commit()
        return user
    
    except:

        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def authenticate_user(data: user.LoginModel, db: Session) -> User | None:
    try:
        user = (
            db.query(User)
            .filter(User.email == data.email, User.name == data.name)
            .first()
        )
        
        if not user:
            return None

        if not security.verify_password(data.password, str(user.password)):
            return None

        return user

    except Exception:
        # traceback.print_exc()
        return None