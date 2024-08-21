from ninja import Router, Schema, Field
from typing import Optional


class UserProfile(Schema):
    username: str = Field(..., min_length=1, max_length=30, required=True)
    email: str = Field(..., min_length=1, max_length=60, required=True)
    password: str = Field(..., min_length=6, required=True)
    is_organizator: bool
    age: Optional[int] = None
    city: Optional[str] = ''
    work_experience: Optional[int] = None

class Error(Schema):
    details: str

class UserSignin(Schema):
    email: str = Field(..., min_length=1, max_length=60, required=True)
    password: str = Field(..., min_length=6, required=True)

class Token(Schema):
    token: str

