from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
from databases import Database


DATABASE_URL = "postgresql+psycopg2://postgres:123@localhost:5432/post"


database = Database(DATABASE_URL)

engine = create_engine(DATABASE_URL, echo=True)
metadata_obj = MetaData()
metadata_obj.create_all(engine)