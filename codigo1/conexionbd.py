"""
Ejemplo para mantener una conexión con la BD en una clase.
Utilizar el destructor para cerrar la conexión.
"""

import sqlite3 as db
from os.path import isfile
import json

class Conexion:

    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"el fichero: {path} no existe")
        else:
            self.con = db.connect(path)

    def query(self, sql):
        cur = None
        try:
            cur = self.con.cursor()
            cur.execute(sql)
            cabs = tuple([t[0] for t in cur.description])
            print(cabs)
            L = [t for t in cur.fetchall()]
            L.insert(0, cabs)           
            return L

        except Exception as e:
            print(e)
        finally:
            if cur:
                cur.close()

    def __del__(self):
        if hasattr(self, "con"):            
            self.con.close()


def convertirJson(L, path):
    fich = None
    try:
        fich = open(path, "w")


    except Exception as e:
        print(e)

    finally:
        if fich:
            fich.close()
    

if __name__ == "__main__":
    try:
        conexion = Conexion("../BBDD/empresa3.db")
        L = conexion.query("select * from empresasenvios")

    except  Exception as e:
        print(e)
