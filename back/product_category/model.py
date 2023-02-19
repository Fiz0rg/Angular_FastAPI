from ormar import Model, Integer, String

from db import database, metadata_obj


class Category(Model):
    class Meta:
        tablename = "category"
        database = database
        metadata = metadata_obj
        

    id: int = Integer(primary_key=True)
    name: str = String(max_length=30)