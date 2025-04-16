from pydantic import BaseModel

class Item():
    name: str #ERROR FIX: changed int to str
    description: str
    _id:str #Item needs to have name description and id 
class User(BaseModel):
    username: str
    bio: str
    
    # You can raise your hands and give the answer to the chocolate question
