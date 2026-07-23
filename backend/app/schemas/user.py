
from pydantic import BaseModel, Field

class UserModel(BaseModel):
    name: str = Field(max_length=60)
    email: str = Field(max_length=50)
    bio: str | None = Field(max_length=200)
    password: str = Field(min_length=8)



class LoginModel(BaseModel):
    name: str
    email:str
    password: str



class Data(BaseModel):
    name: str
    email: str
    bio: str | None = None
    

class LoginResponse(BaseModel):
    msg: str
    data: Data
    
    class config:

        from_attributes = True

