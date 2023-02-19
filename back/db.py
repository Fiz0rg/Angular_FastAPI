import dotenv

from sqlalchemy import create_engine, MetaData
from databases import Database

dotenv.load_dotenv('.env')

DATABASE_URL = "postgresql+psycopg2://postgres:123@habr:5432/postgres"

database = Database(DATABASE_URL)

engine = create_engine(DATABASE_URL, echo=True)
metadata_obj = MetaData()
metadata_obj.create_all(engine)