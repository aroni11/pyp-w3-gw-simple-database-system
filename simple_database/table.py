import os
import json

from .exceptions import ValidationError
from .config import BASE_DB_FILE_PATH
from datetime import date

class Table(object):
    
    def __init__(self, db_name, table_name, columns):
        self.name = table_name
        self.path = os.path.join(BASE_DB_FILE_PATH, db_name, table_name)    #/tmp/simple_database/db_name
        self.structure = {}
        self.structure['structure'] = columns
        self.structure['data'] = {}
        self._create_json_file()
        
        
    def _create_json_file(self):
        with open(self.path, 'w+') as fout:
            data = json.dumps(self.structure, fout)
            fout.write(data)
            fout.close
    
    
    def _build_data_from_args(self, *args):
        new_data = self.structure['data']
        index = 0
        
        for item in self.structure['structure']:
            name = item['name']
            if isinstance(args[0][index], date):
                value = str(args[0][index])
            else:
                value = args[0][index]
            new_data[name] = value
            index += 1
            
        return new_data
    
    """
    def _check_structure(self, *args):
        correct_structure = self.structure['structure']
        new_dict = self._build_data_from_args(args)
        missing_count = len(correct_structure) - len(new_dict)
        
        if missing_count == 0:
            return True
        else:
            return False
    """        
        
    def insert(self, *args):
        """
        if not self._check_structure(self, args):
            raise TypeError('Missing some of arguments to match structure.')
        """
        
        insert_data = self._build_data_from_args(args)
        with open(self.path, 'a+') as fout:
            fout.write(json.dumps(insert_data))


    def count(self):
        counter = 0
        
        for item in self.structure['data'].items():
            counter += 1
            
        return counter