from .Database import Database

def create_database(db_name):
    return Database(db_name)

def connect_database(db_name):
    raise NotImplementedError()
