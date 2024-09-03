"""
Extraer datos (DF) de una BD con pandas y exportar a JSON
"""

import pandas as pd
from os.path import isfile
import sqlite3 as dbapi


class BaseDatos:

    def __init__(self, path):

        if not isfile(path):
            raise FileNotFoundError("No se encuentra el fichero: " + path)
        else:
            self.con = dbapi.connect(path)
            # print('Base de datos abierta!')

    def getDF(self, sql):
        return pd.read_sql(sql, self.con)

    def __del__(self):
        if hasattr(self, "con"):
            self.con.close()


if __name__ == "__main__":
    bd = BaseDatos("../BBDD/empresa3.db")
    sql = """select c.nombre as categoria,
    count(p.id) as numproductos from categorias c inner join 
    productos p on c.id = p.idcategoria group by c.nombre
    order by 2 desc"""
    df = bd.getDF(sql)
    df.to_json("../ficheros/categorias.json", indent=4, orient="records")
    dfPed = bd.getDF("select * from pedidos")
    dfPed.to_json("../ficheros/pedidos.json", indent=4, orient="records")

    sql = """select c.nombre as categoria from categorias c 
    inner join productos p on c.id = p.idcategoria order by p.id"""
    df2 = bd.getDF(sql)
    print("Con repetidos: ", df2.shape)
    #print(df2.head(15))
    df3 = df2.drop_duplicates()
    print("Sin repetidos: ",df3.shape)

    # Iterar por las filas de un DF:
    i = 3
    for index, pedido in dfPed.iterrows():
        print(index, pedido.values)    
        i-=1
        if i == 0:break
