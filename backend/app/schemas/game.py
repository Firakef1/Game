from sqlalchemy import Column, UUID, ForeignKey
from uuid6 import uuid7
from core.database import Base

class Game(Base):
    __tablename__ = "game"

    game_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid7)

    user_one_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), index=True, nullable=False)
    user_two_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), index=True, nullable=False)

    winner_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=True)