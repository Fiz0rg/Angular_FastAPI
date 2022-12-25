from ormar import Model, Integer, String

from .base_class import MetaClass


class Category(Model):
    class Meta(MetaClass):
        tablename = "category"
        

    id: int = Integer(primary_key=True)
    name: str = String(max_length=30)