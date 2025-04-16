from pydantic import BaseModel

class Item():
    name: int
    description: str

class User(BaseModel):
    username: str
    bio: str
    
    # You can raise your hands and give the answer to the chocolate question
class QuizAnswer(BaseModel):
    id: int
    answer: str
    score: int