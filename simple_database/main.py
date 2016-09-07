import os

from .config import BASE_DB_FILE_PATH
from .exceptions import ValidationError

from .database import Database

def create_database(db_name):
    return Database(db_name)

def connect_database(db_name):
    if os.path.exists(os.path.join(BASE_DB_FILE_PATH, db_name)):
        return Database(db_name)
    else:
        raise ValidationError("This database does not exist")
