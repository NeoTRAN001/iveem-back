from pydantic import Field, BaseModel


class UserJWTSchema(BaseModel):
    username: str = Field(...),
    rol: str = Field(...)
