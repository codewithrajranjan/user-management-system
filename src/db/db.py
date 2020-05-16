from pymongo import MongoClient
from src.config.config import ConfigManager

database_host = ConfigManager.get_config("DATABASE_HOST")
database_port = ConfigManager.get_config("DATABASE_PORT")
database_name = ConfigManager.get_config("DATABASE_NAME")

connection_string = "mongodb://{}:{}/{}".format(database_host, database_port, database_name)

client = MongoClient(connection_string)
db_connection_ref = client[ConfigManager.get_config("DATABASE_NAME")]


class DB:
    @classmethod
    def get_connection(cls):
        return db_connection_ref
