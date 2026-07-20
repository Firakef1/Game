from fastapi import FastAPI
from app.crud import crud_user
app = FastAPI()

app.include_router(crud_user.router)

@app.get("/")
def root():
    print("HELLO")
    return {"status": "Game backend is fully operational!"}