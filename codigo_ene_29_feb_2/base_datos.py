"""
Clase para conectar con la BD.
"""
import sqlite3 as dbapi
from objetos import Empleado
from os.path import isfile

class BaseDatos:

    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"No se encuentra el fichero {path}")

        else:
            self.con = dbapi.connect(path)

    def __del__(self):
        if hasattr(self, "con"):
            self.con.close()

if __name__=='__main__':
    try:
        bd = BaseDatos('no existe.dat')
    except Exception as e:
        print(e.__class__.__name__, e)

