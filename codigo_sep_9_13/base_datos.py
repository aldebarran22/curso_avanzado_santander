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
        if hasattr(self, 'conexion'):
            print('cerrando conexión')
            self.conexion.close()

if __name__ == '__main__':
    try:
        bd = BaseDatos("../BBDD/empresa3.db")

    except Exception as e:
        print(e)