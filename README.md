# Fastapi-Training
Learn restful API using [FastAPI](https://fastapi.tiangolo.com/) framework and postgresql

## How to run ?
> uvicorn main:app --reload

## Getting Started

1. Install fastapi `pip install fastapi`
2. Install uvicorn `pip install uvicorn` as ASGI server
3. Install sqlalchemy `pip install sqlalchemy`
4. Install databases driver `pip install databases`
5. Install asyncpg driver `pip install asyncpg`
6. Install pydantic driver `pip install pydantic`
7. Install typing `pip install typing`


## Config Database

We use [**postgresql**](https://www.postgresql.org/) as the database :
````
DB_URL = 'postgresql://{YOUR POSTGRE USERNAME}:{YOUR POSTGRE PASSWORD}@127.0.0.1:{YOUR PORT SET ON POSTGRE}/{YOUR DB NAME}'
````
