from typing import Optional, List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import databases, sqlalchemy
from sqlalchemy import and_
from model.User import UserRegister, User, UserLogin, UserProfile


# CONFIG DB PostgreSQL
DB_URL = 'postgresql://postgres:root@127.0.0.1:5432/testing'
database = databases.Database(DB_URL)
metadata = sqlalchemy.MetaData()

#Create Schema
user = sqlalchemy.Table(
    "user",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("username", sqlalchemy.String(50), unique=True, nullable=False),
    sqlalchemy.Column("email", sqlalchemy.String(100), unique=True, nullable=False),
    sqlalchemy.Column("password", sqlalchemy.String(100), nullable=False),
    sqlalchemy.Column("first_name", sqlalchemy.String(100), nullable=False),
    sqlalchemy.Column("last_name", sqlalchemy.String(100), nullable=False),
    sqlalchemy.Column("img_url", sqlalchemy.String(200), nullable=True),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=sqlalchemy.func.now()),
)

engine = sqlalchemy.create_engine(
    DB_URL
)
metadata.create_all(engine)


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event('startup')
async def startup():
    await database.connect()

@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/user", response_model=List[User])
async def getAllUser():
    query = user.select()
    return await database.fetch_all(query)

@app.post("/user/login", response_model=User)
async def login(payload : UserLogin):
    query = user.select().where(and_(user.c.username == payload.username, user.c.password == payload.password))
    result = await database.fetch_one(query)

    if(result): return result 
    else: return { "msg" : "Data Not Found !" }

@app.get("/user/{userID}", response_model=User)
async def getUser(userID:int):
    query = user.select().where(user.c.id == userID)
    return await database.fetch_one(query)

@app.put("/user/edit/{userID}", response_model=User)
async def login(userID : int, payload: UserProfile):
    query = user.update().where(user.c.id == userID).values(
        username = payload.username,
        img_url = payload.img_url,
        first_name = payload.first_name,
        last_name = payload.last_name,
        email = payload.email
    )
    result = await database.execute(query)

    return await getUser(userID)

@app.post("/user/", response_model=UserRegister)
async def registerUser(payload : UserRegister):
    query = user.insert().values(
        username = payload.username,
        password = payload.password,
        first_name = payload.first_name,
        last_name = payload.last_name,
        email = payload.email
    )
    await payloadbase.execute(query)
    return {
        **payload.dict(),
        'status' : True
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}