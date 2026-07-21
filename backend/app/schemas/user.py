
from pydantic import BaseModel, Field

class User_model(BaseModel):
    name: str = Field(max_length=60)
    email: str = Field(max_length=50)
    bio: str | None = Field(max_length=200)