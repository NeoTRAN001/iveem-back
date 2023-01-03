from pydantic import Field, EmailStr, BaseModel
from typing import Optional


class UserProfileSchema(BaseModel):
    email: EmailStr = Field(...)
    name: str = Field(..., max_length=50, min_length=3)
    lastname: str = Field(..., max_length=50, min_length=3)
    username: str = Field(..., max_length=50, min_length=3)
    birthday: str = Field(...)
    picture: Optional[str] = None
    rol: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "email": "account@email.com",
                "name": "name",
                "username": "username",
                "lastname": "lastname",
                "birthday": "2000-01-01",
                "picture": "https://url.png"
            }
        }