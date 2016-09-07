import os
import json

from .exceptions import ValidationError
from .config import BASE_DB_FILE_PATH

class Table(object):
    
    def __init__(self, db_name, table_name, columns):
        self.name = table_name
        self.path = os.path.join(BASE_DB_FILE_PATH, db_name, table_name)    #/tmp/simple_database/db_name
        self.structure['structure'] = columns
        self._create_json_file()
        
        
    def _create_json_file(self):
        with open(self.path, 'w+') as fout:
            data = json.dump(self.structure, fout)
            fout.write(data)
            fout.close
    
    
    def _build_data_from_args(*args):
        new_data = {}
        count = 0
        
        for item in self.structure['structure']:
            name = item['name']
            if type(args[count]) is date:
                value = str(args[count])
            else:
                value = args[count]
            new_data[name] = value
            
        return new_data
    
    
    def _check_structure(self, *args):
        correct_structure = self.structure
        new_dict = self._build_dict_from_args(args)
        missing_count = len(correct_structure) - len(new_dict)
        
        if missing_count == 0:
            return True
        else:
            return False
            
        
    def insert(self, *args):
        if not _check_structure(self, args, self.structure):
            raise TypeError('Missing some of arguments to match structure.')
        
        insert_data = self._build_data_from_args(args)
        with open(self.path, 'a+') as fout
            table = json.load(fout)
            table['data'].append(insert_data)
        
   
    
    def count(self):
        pass
    