from sqlalchemy import Column, String, UUID
from uuid6 import uuid7
from  app.core.database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid7, index=True)

    email = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    bio = Column(String, nullable=True)