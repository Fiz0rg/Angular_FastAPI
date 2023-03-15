from ormar import String, Integer, Model, Boolean, DateTime

from db import database, metadata_obj

class Buyer(Model):
    class Meta:
        tablename = "buyer"
        database = database
        metadata = metadata_obj

    id: int = Integer(primary_key=True)
    username: str = String(max_length=30, unique=True)
    gmail: str = String(max_length=100, unique=True)
    password: str = String(max_length=100)
    is_admin: bool = Boolean(default=False)
    is_activate: bool = Boolean(default=False)
    creation_datetime: str = DateTime(nullable=True)
