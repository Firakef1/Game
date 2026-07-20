from uuid6 import uuid7
from sqlalchemy import create_engine, Column, Integer, String, UUID, ForeignKey
from sqlalchemy.orm import declarative_base

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid7, index=True)

    email = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    bio = Column(String)

class Game(Base):
    __tablename__ = "game"

    game_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid7)

    user_one_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), index=True, nullable=False)
    user_two_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), index=True, nullable=False)

    winner_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=True)

class UserGameStats(Base):
    __tablename__ = "user_game_stats"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), primary_key=True)

    count = Column(Integer, default=0, nullable=False)
    finished = Column(Integer, default=0, nullable=False)
    aborted = Column(Integer, default=0, nullable=False)
    won = Column(Integer, default=0, nullable=False)
    lost = Column(Integer, default=0, nullable=False)
    draw = Column(Integer, default=0, nullable=False)

