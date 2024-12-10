"""
Conexión a la BD con control de excepciones
"""

import sqlite3 as db
from os.path import isfile

class BaseDatos:
    
    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero: {path}")
        else:
            self.con = db.connect(path)

    def __del__(self):
        self.con.close()

if __name__ == '__main__':
    try:
        bd = BaseDatos("../BBDD/empresa3.db")
        
    except Exception as e:
        print(e)