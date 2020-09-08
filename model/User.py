from pydantic import BaseModel, Field
from datetime import datetime

class User(BaseModel):
    id : str
    username : str
    email : str
    password:str
    first_name:str
    last_name:str
    img_url:str = None
    created_at:datetime

class UserRegister(BaseModel):
    username : str
    email : str
    password:str
    first_name:str
    last_name:str

class UserLogin(BaseModel):
    username : str
    password:str

class UserProfile(BaseModel):
    username : str
    email : str
    img_url:str = None
    first_name:str
    last_name:str