import os
import json

from .config import BASE_DB_FILE_PATH
from .table import Table

class Database(object):
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.tables = []
        self.path = os.path.join(BASE_DB_FILE_PATH, db_name)
        
        if not self._check_if_db_exists(db_name):
            os.makedirs(self.path)

    
    def _check_if_db_exists(self,db_name):
        if os.path.exists(self.path):
            return True
        else:
            return False


    def create_table(self, name, columns):
        new_table = Table(self.db_name, name, columns)
        self.tables.append(name)
        setattr(self, name, new_table)
        
    
    def show_tables(self):
        return self.tables    