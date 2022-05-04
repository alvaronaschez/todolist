from typing import TypeVar

from .models import UserCredentials, UserRead, UserCreate, UserUpdate


Token = TypeVar("Token", bound=str)


def register_user(user: UserCreate):
    raise NotImplementedError()


def login(credentials: UserCredentials) -> Token:
    raise NotImplementedError()


def logout(token: Token):
    raise NotImplementedError()


def me(token: Token) -> UserRead:
    raise NotImplementedError()


def update_user(user: UserUpdate, token: Token):
    raise NotImplementedError()


def delete_user(token: Token):
    raise NotImplementedError()
