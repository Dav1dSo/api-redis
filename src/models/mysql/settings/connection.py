import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

class DBConnectionHandler:
    def __init__(self) -> None:
        self._connection_string = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
        self._conn = None

    def connect(self) -> None:
        self._conn = create_engine(self._connection_string)

    def get_connection(self):
        return self._conn
    
db_connection_handler = DBConnectionHandler()
db_connection_handler.connect()