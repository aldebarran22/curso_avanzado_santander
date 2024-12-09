"""
Ejemplo para mantener una conexión con la BD en una clase.
Utilizar el destructor para cerrar la conexión.
"""

import sqlite3 as db
from os.path import isfile

class Conexion:

    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"el fichero: {path} no existe")        
        else:
            self.con = db.connect(path)


    def __del__(self):
        self.con.close()

    
if __name__ == '__main__':
    conexion = Conexion('empresa3.db')





