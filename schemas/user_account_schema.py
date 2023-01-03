from pydantic import Field, BaseModel, EmailStr


class UserAccountSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(
        ...,
        min_length=8,
        max_length=100
    )

    class Config:
        schema_extra = {
            "example": {
                "email": "account@email.com",
                "password": "123456789"
            }
        }