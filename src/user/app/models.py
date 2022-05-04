import re
from datetime import date
from pydantic import BaseModel as PydanticBaseModel, EmailStr, Field, validator


class BaseModel(PydanticBaseModel):
    class Config:
        allow_mutation = False
        orm_mode = True


class UserCredentials(BaseModel):
    username: str
    password: str


class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=30)
    password: str = Field(min_length=8, max_length=128)
    email: EmailStr | None
    birth_date: date | None
    first_name: str | None
    last_name: str | None

    @validator("password")
    def validate_password(cls, v):
        if not re.search("[A-Z]", v):
            raise ValueError("must contain a capital letter")
        if not re.search("[a-z]", v):
            raise ValueError("must contain a lowercase letter")
        if not re.search("[0-9]", v):
            raise ValueError("must contain a digit")
        SPECIAL_CHARS_PATTERN = r"[ !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]"
        if not re.search(SPECIAL_CHARS_PATTERN, v):
            raise ValueError("must contain an special character")


class UserRead(BaseModel):
    username: str
    email: EmailStr | None
    birth_date: date | None
    first_name: str | None
    last_name: str | None


class UserUpdate(BaseModel):
    email: EmailStr | None
    birth_date: date | None
    first_name: str | None
    last_name: str | None
