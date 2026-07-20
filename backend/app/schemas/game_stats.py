from sqlalchemy import Column, UUID, Integer, ForeignKey
from core.database import Base


class UserGameStats(Base):
    __tablename__ = "user_game_stats"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), primary_key=True)

    count = Column(Integer, default=0, nullable=False)
    finished = Column(Integer, default=0, nullable=False)
    aborted = Column(Integer, default=0, nullable=False)
    won = Column(Integer, default=0, nullable=False)
    lost = Column(Integer, default=0, nullable=False)
    draw = Column(Integer, default=0, nullable=False)