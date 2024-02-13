"""
Implementar las operaciones CRUD para una entidad
de la base de datos
C - Create: insert into
R - Read: select ... where id=PK
U - Update: update
D - Delete: delete
select: select all
"""

import sqlite3 as db
from os.path import isfile


class Empleado:
    def __init__(self, id=0, nombre="", cargo=""):
        self.__id = id
        self.__nombre = nombre
        self.__cargo = cargo

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getCargo(self):
        return self.__cargo

    def setCargo(self, cargo):
        self.__cargo = cargo

    def getTupla(self):
        return (self.__nombre, self.__cargo)

    def getTupla2(self):
        return (self.__nombre, self.__cargo, self.__id)

    def __str__(self):
        return str(self.__id) + " " + self.__nombre + " " + self.__cargo

    def __repr__(self):
        return str(self)


class BaseDatos:

    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"El fichero {path} no existe")

        self.con = db.connect(path)

    def create(self, empleado):
        cur = None
        try:
            cur = self.con.cursor()
            sql = "insert into empleados(nombre,cargo) values(?,?)"
            cur.execute(sql, empleado.getTupla())
            # El id generado por la BD
            empleado.setId(cur.lastrowid)
            n = cur.rowcount
            self.con.commit()
            if n == 0:
                raise ValueError(f"No se ha podido crear el empleado")
            else:
                return n == 1

        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            if cur:
                cur.close()

    def update(self, emp):
        cur = None
        try:
            cur = self.con.cursor()
            sql = "update empleados set nombre=?,cargo=? where id=?"
            cur.execute(sql, emp.getTupla2())
            n = cur.rowcount  # Número de regs. afectados!
            self.con.commit()
            return n > 0

        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            if cur:
                cur.close()

    def delete(self, id):
        cur = None
        try:
            cur = self.con.cursor()
            sql = "delete from empleados where id=?"
            cur.execute(sql, (id,))
            n = cur.rowcount  # Número de registros eliminados
            self.con.commit()
            if n == 0:
                # No existe el registro
                raise ValueError(f"El empleado: {id} no existe")
            else:
                return n == 1

        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            if cur:
                cur.close()

    def read(self, id):
        cur = None
        try:
            cur = self.con.cursor()
            sql = "select * from empleados where id=?"
            cur.execute(sql, (id,))
            t = cur.fetchone()
            if t:
                return Empleado(*t)
            else:
                raise ValueError(f"El empleado: {id} no existe")

        except Exception as e:
            raise e
        finally:
            if cur:
                cur.close()

    def select(self, cargo=None):
        cur = None
        try:
            cur = self.con.cursor()
            sql = f"select * from empleados "
            if cargo:
                sql += "where cargo=?"
                cur.execute(sql, (cargo,))
            else:
                cur.execute(sql)

            return [Empleado(*t) for t in cur.fetchall()]
        except Exception as e:
            raise e
        finally:
            if cur:
                cur.close()

    def __del__(self):
        if hasattr(self, "con"):
            print("conexión cerrada...")
            self.con.close()


if __name__ == "__main__":
    try:
        bd = BaseDatos("../bd/empresa3.db")
        L = bd.select("Gerente")
        print(L)

        obj = bd.read(14)
        print(obj)

        obj.setCargo("Presidente")
        if bd.update(obj):
            print("Registro actualizado")

        """
        

        id = 29
        if bd.delete(id):
            print(f"El empleado: {id} eliminado")
        """

        """
        emp = Empleado(0, "Andrés", "Gerente de ventas")
        bd.create(emp)
        print(emp)
        """

    except Exception as e:
        print(e)
