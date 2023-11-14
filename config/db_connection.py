import databases
import sqlalchemy
from decouple import config

DATABASE_URL = f"mysql+pymysql://{config('SQL_DB_USER')}:{config('SQL_DB_PASSWORD')}@localhost:3306/{config('SQL_DATABASE_NAME')}"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


class SqlDatabase:
    @staticmethod
    async def create_connection():
        await database.connect()

    @staticmethod
    async def close_connection():
        await database.disconnect()
