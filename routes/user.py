from fastapi import APIRouter
from config.db import conn
from models.index import user
from schemas.index import User
    

user = APIRouter()

@user.get("/")
async def read_data():
    return conn.execute(user.select()).fetchall()

@user.get("/{id}")
async def get_user(id:int):
    return conn.execute(user.select().where(user.c.id==id)).fetchall()

@user.post("/user/{id}")
async def create_user(user:User,id:int):
    #conn.execute(user.insert().values(name = user.name,password = user.password,email = user.email))    
    return {"response":{"user":"name"}}


@user.put("/update/{id}")
async def upadte_user(id:int,user:User ):
    conn.execute(user.update(name = user.name,password = user.password,email = user.email)).where(user.c.id==id)
    return conn.execute(user.select()).fetchall()


@user.delete("/del/{id}")
async def delete_user(id:int,user:User):
    conn.execute(user.delete().where(user.c.id==id))
      













 









