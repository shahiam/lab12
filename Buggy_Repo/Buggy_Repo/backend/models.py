from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str #ERROR FIX: changed int to str
    description: str
    _id: Optional[str] = None

class User(BaseModel):
    username: str
    bio: str
    _id: Optional[str] = None

class QuizAnswer(BaseModel):
    id: int
    answer: str
    score: int
    
    # You can raise your hands and give the answer to the chocolate question
