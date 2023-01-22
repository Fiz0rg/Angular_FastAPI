from db.category import Category


class RepositoryClass:

    async def get_all_caregories():
        return await Category.objects.all()

    
    def test(name: str):
        return name