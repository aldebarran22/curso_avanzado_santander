"""
Extraer dataframes de una BD.
"""

import sqlite3 as db
import pandas as pd
from os.path import isfile


class BaseDatos:

    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero: {path}")

        self.con = db.connect(path)

    def getDataFrame(self, sql):
        return pd.read_sql(sql, self.con)

    def __del__(self):
        if hasattr(self, "con"):
            self.con.close()


if __name__ == "__main__":
    try:
        baseDatos = BaseDatos("../BBDD/empresa3.db")
        sql = """select p.id as idprod, c.nombre, p.nombre, 
        p.precio, p.existencias from productos p inner join
        categorias c on p.idcategoria = c.id"""
        df = BaseDatos.getDataFrame(sql)
        print(df.head())

    except Exception as e:
        print(e)
