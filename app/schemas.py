from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel


class PasswordChange(SQLModel):
    old_password: str
    new_password: str


class LoginRequest(SQLModel):
    username: str
    password: str


class TokenResponse(SQLModel):
    access_token: str
    token_type: str = "bearer"


class UserBase(SQLModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


UserRead = UserResponse


class UserUpdate(SQLModel):
    email: Optional[str] = None