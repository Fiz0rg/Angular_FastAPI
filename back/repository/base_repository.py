class BaseRepository:

    async def create_object(new_object, db_model):
        return await db_model.objects.create(**new_object.dict())