"""
Extraer información de la BD con pandas
"""

import pandas as pd
import sqlite3 as db


def extraerDF(path, sql):
    pass


if __name__ == "__main__":
    sql = """SELECT idcliente, 
    sum(importe)  as total
    FROM pedidos
    group by idcliente
    order by 2 desc"""
    df = extraerDF("../BBDD/empresa3.db", sql)
