"""
Extraer información de la BD con pandas
"""

import pandas as pd
import sqlite3 as db
from os.path import isfile


def extraerDF(path, sql):
    con = None
    try:
        if isfile(path):
            con = db.connect(path)
            return pd.read_sql(sql, con)
        else:
            raise FileNotFoundError(f"No existe el fichero: {path}")
    except Exception as e:
        print(e)
    finally:
        if con:
            con.close()


if __name__ == "__main__":
    sql = """SELECT idcliente, 
    sum(importe)  as total
    FROM pedidos
    group by idcliente
    order by 2 desc"""
    df = extraerDF("../BBDD/empresa3.db", sql)
    print(df.head())
