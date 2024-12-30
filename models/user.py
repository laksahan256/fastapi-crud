from sqlalchemy import Table, Column, Integer, String, MetaData

from config.db import meta

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(50)),
    Column("email", String(50)),
    Column("password", String(50)),
)