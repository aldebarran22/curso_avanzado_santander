"""
Clase para conectar con la BD y dejar cerrada 
la conexión.
"""
import sqlite3 as dbapi
from os.path import isfile

class BaseDatos:

    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"El fichero: {path} no existe")
        
        # Abrir la conexion
        self.conexion = dbapi.connect(path)

    def __del__(self):
        self.conexion.close()

if __name__ == '__main__':
    bd = BaseDatos("../BBDD/empresa3.db")