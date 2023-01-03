from pydantic import Field, PastDate
from typing import Optional
from schemas.user_account_schema import UserAccountSchema


class UserAccountRegisterSchema(UserAccountSchema):
    name: str = Field(..., max_length=50, min_length=3)
    lastname: str = Field(..., max_length=50, min_length=3)
    username: str = Field(..., max_length=50, min_length=3)
    birthday: str = Field(...)
    picture: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "email": "account@email.com",
                "password": "123456789",
                "name": "name",
                "username": "username",
                "lastname": "lastname",
                "birthday": "2000-01-01",
                "picture": "https://url.png"
            }
        }
