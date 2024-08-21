from ninja import Router, Schema, Field
from typing import Optional, List

class Project(Schema):
    name: str = Field(..., max_length=200, required=True)
    resume_id: int
    description: str

class Error(Schema):
    details: str
