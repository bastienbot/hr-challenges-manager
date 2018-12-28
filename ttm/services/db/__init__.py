from .files import DBFiles


class DBConnector:

    def __new__(cls, db_type="files"):
        if db_type == "files":
            return DBFiles()
        else:
            return DBFiles()
