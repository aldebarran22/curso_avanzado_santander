"""
Conexión a la Base de datos
"""

import sqlite3 as db
from os.path import isfile

class BaseDatos:

    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"El fichero: {path} no existe")
        
        self.con = db.connect(path)

    def __del__(self):
        if hasattr(self, "con"):
            print('Cerrando base de datos')
            self.con.close()


if __name__=='__main__':
    try:
        bd  = BaseDatos("../BBDD/empresa3.db")
    except Exception as e:
        print(e.__class__.__name__, e)