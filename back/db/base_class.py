from ormar import ModelMeta

from .db import metadata_obj, database

"""
Database = created with my db.DATABASE_URL in sqlalchemy connection string format
MetaData = container object that keeps together many different features of a database (or multiple databases) being described.
"""


class MetaClass(ModelMeta):
    database = database
    metadata = metadata_obj