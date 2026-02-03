from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class IdeaBase(BaseModel):
    title: str
    description: Optional[str] = None

class IdeaCreate(IdeaBase):
    pass

class IdeaUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class Idea(IdeaBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True