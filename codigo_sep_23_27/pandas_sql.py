"""
Extraer dataframes de una BD.
"""
import sqlite3 as db
from os.path import isfile

class BaseDatos:

    def __init__(self,path):
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero: {path}")
        
        self.con = db.connect(path)        

    
    def __del__(self):
        print('Cerrar BD')
        self.con.close()

if __name__ == '__main__':
    baseDatos = BaseDatos("../BBDD/empresa3.db")
