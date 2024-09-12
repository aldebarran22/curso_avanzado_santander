"""
Clase para conectar con la BD y dejar cerrada 
la conexión.
"""

import sqlite3 as dbapi
from os.path import isfile
import pandas as pd


class BaseDatos:

    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"El fichero: {path} no existe")

        # Abrir la conexion
        self.conexion = dbapi.connect(path)

    def getDataFrame(self, sql):
        return pd.read_sql(sql, self.conexion)

    def __del__(self):
        if hasattr(self, "conexion"):
            print("cerrando conexión")
            self.conexion.close()


if __name__ == "__main__":
    try:
        bd = BaseDatos("../BBDD/empresa3.db")
        sql = """select c.nombre as categoria, count(p.id) as cuenta
            from categorias c inner join productos p
            on c.id = p.idcategoria
            group by c.nombre
            order by c.nombre"""
        df = bd.getDataFrame(sql)
        print(df)

    except Exception as e:
        print(e)
