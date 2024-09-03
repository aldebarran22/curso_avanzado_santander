"""
Clase para conectar con la BD.
"""
import sqlite3 as dbapi
from objetos import Empleado
from os.path import isfile


class BaseDatos:
    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"No se encuentra el fichero {path}.")

        else:
            self.con = dbapi.connect(path)

    def selectEmpleados(self):
        cur = None
        try:
            cur = self.con.cursor()
            sql = "select id, nombre, cargo from empleados"
            cur.execute(sql)
            return [Empleado(*t) for t in cur.fetchall()]
        except Exception as e:
            print(e)
        finally:
            if cur:
                cur.close()

    def __del__(self):
        if hasattr(self, "con"):
            self.con.close()


if __name__ == "__main__":
    try:
        bd = BaseDatos("../BBDD/empresa3.db")
        L = bd.selectEmpleados()
        L.sort()
        print(L)
    except Exception as e:
        print(e.__class__.__name__, e)

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

    def selectEmpleados(self):
        cur = None
        try:
            cur = self.con.cursor()
            sql = "select id, nombre, cargo from empleados"
            cur.execute(sql)
            return [Empleado(*t) for t in cur.fetchall()]
        except Exception as e:
            print(e)
        finally:
            if cur:
                cur.close()

    def __del__(self):
        if hasattr(self, "con"):
            self.con.close()


if __name__ == "__main__":
    try:
        bd = BaseDatos("../BBDD/empresa3.db")
        L = bd.selectEmpleados()
        L.sort()
        print(L)
    except Exception as e:
        print(e.__class__.__name__, e)
