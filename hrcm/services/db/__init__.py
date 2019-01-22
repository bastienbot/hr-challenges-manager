import os
from .files import DBFiles
from .mongo import DBMongo


class DBConnector:

    def __new__(cls):
        db_type = os.getenv("DB_TYPE")
        if db_type == "files":
            return DBFiles()
        elif db_type == "mongo":
            return DBMongo()
        else:
            return DBFiles()
