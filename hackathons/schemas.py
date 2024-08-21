from accounts.models import Account
from profiles.schemas import UserProfile
from .models import Hackathon
from ninja.orm import create_schema
from ninja import Schema
from typing import List, Optional


class HackathonSchema(Schema):
    id: int
    creator_id: int
    name: str
    image_cover: str
    description: str
    min_participants: Optional[int]
    max_participants: Optional[int]
    participants: List[UserProfile]

class HackathonIn(Schema):
    name: str
    description: str
    min_participants: int
    max_participants: int
    participants: List[str]

class HackathonOut(Schema):
    creator: int
    name: str
    description: str
    participants: List[str]
    imave_cover: str
    min_participants: int 
    max_participants: int

class EditHackathon(Schema):
    name: Optional[str] = ''
    description: Optional[str] = ''
    min_participants: Optional[int] = None
    max_participants: Optional[int] = None

class Error(Schema):
    details: str
    
class AddUserToHack(Schema):
    email: str

class StatusOK(Schema):
    status: str = 'ok'