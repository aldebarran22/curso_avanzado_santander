"""
Conexión a la Base de datos
"""

import sqlite3 as db
from os.path import isfile
import pandas as pd

class BaseDatos:

    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"El fichero: {path} no existe")
        
        self.con = db.connect(path)

    def getDataFrame(self, sql):
        return pd.read_sql(sql, self.con)

    def __del__(self):
        if hasattr(self, "con"):            
            self.con.close()


if __name__=='__main__':
    sql = """select p.id as idprod, p.nombre, c.nombre as categoria,
    p.precio, p.existencias from categorias c inner join productos p
    on p.idcategoria = c.id"""
    try:
        bd  = BaseDatos("../BBDD/empresa3.db")
        df = bd.getDataFrame(sql)
        print(df.head())
        df.to_json("../ficheros/productos.json", indent=4, orient="records")
    except Exception as e:
        print(e.__class__.__name__, e)