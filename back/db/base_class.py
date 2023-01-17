from ormar import ModelMeta

from .db import metadata_obj, database


class MetaClass(ModelMeta):
    database = database
    metadata = metadata_obj