from pydantic import BaseModel
from typing import List
from typing import Optional

class Blog(BaseModel):
    title: str
    body: str
    
class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    id: int
    blogs: List[Blog] = []

class ShowBlog(Blog):
    id: int
    created_by: ShowUser

    # class Config():
    #     orm_mode = True
    
class Login(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
