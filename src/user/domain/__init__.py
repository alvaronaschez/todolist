from datetime import date
from pydantic import (
    BaseModel as PydanticBaseModel,
    EmailStr,
    # Field,
    # validator,
)

# entities


class BaseModel(PydanticBaseModel):
    class Config:
        allow_mutation = False
        orm_mode = True


class User(BaseModel):
    id: int
    hashed_password: str
    username: str
    email: EmailStr | None
    birth_date: date | None
    first_name: str | None
    last_name: str | None
