from fastapi import FastAPI
from app.crud import crud_user
from app.core.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(crud_user.router)

@app.get("/")
def root():
    print("HELLO")
    return {"status": "Game backend is fully operational!"}