from ormar import String, Integer, Model, Boolean

from .base_class import MetaClass


class Buyer(Model):
    class Meta(MetaClass):
        tablename = "buyer"

    id: int = Integer(primary_key=True)
    username: str = String(max_length=30, unique=True)
    password: str = String(max_length=100)
    is_admin: bool = Boolean(default=False)
