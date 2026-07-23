from fastapi import FastAPI
from app.api.v1.endpoints import users
from app.core.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
