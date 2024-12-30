from fastapi import APIRouter
from sqlalchemy.engine import Row

from models.user import users
from config.db import conn
from schemas.users import User

user = APIRouter()

@user.get("/")
async def read_data():
    result = conn.execute(users.select()).fetchall()
    return [dict(row._mapping) for row in result]


@user.get("/{id}")
async def read_data(id: int):
    result = conn.execute(users.select().where(users.c.id == id)).fetchall()
    return [dict(row._mapping) for row in result]


@user.post("/")
async def write_data(user: User):
    conn.execute(users.insert().values(
        name=user.name,
        email=user.email,
        password=user.password
    ))
    result = conn.execute(users.select()).fetchall()
    return [dict(row._mapping) for row in result]


@user.put("/{id}")
async def update_data(id: int, user: User):
    conn.execute(users.update().values(
        name=user.name,
        email=user.email,
        password=user.password
    ).where(users.c.id == id))
    result = conn.execute(users.select()).fetchall()
    return [dict(row._mapping) for row in result]


@user.delete("/{id}")
async def delete_data(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    result = conn.execute(users.select()).fetchall()
    return [dict(row._mapping) for row in result]