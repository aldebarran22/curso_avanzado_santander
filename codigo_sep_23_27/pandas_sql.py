"""
Extraer dataframes de una BD.
"""

import sqlite3 as db
from os.path import isfile


class BaseDatos:

    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero: {path}")

        self.con = db.connect(path)

    def __del__(self):
        if hasattr(self, "con"):
            self.con.close()


if __name__ == "__main__":
    try:
        baseDatos = BaseDatos("../BBDD/empresa3.db")
    except Exception as e:
        print(e)
