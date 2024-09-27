"""
Implementación de las clases Categoria y Producto
"""

import sqlite3 as dbapi
from os.path import isfile

path = "../../BBDD/empresa3.db"


class Empleado:

    def __init__(self, id=0, nombre="", cargo=""):
        self.id = id
        self.nombre = nombre
        self.cargo = cargo

    def to_json(self):
        return self.__dict__

    def getTupla(self):
        return (self.id, self.nombre, self.cargo)

    @staticmethod
    def create(d):
        return Empleado(**d)
        #return Empleado(d["id"], d["nombre"], d["cargo"])

    def __str__(self):
        return str(self.id) + " " + self.nombre + " " + self.cargo

    def __repr__(self):
        return str(self)


class Categoria:

    __num_instancias = 0

    def __init__(self, id=0, nombre=""):
        self.id = id
        self.nombre = nombre
        Categoria.__num_instancias += 1

    @staticmethod
    def create(d):
        """Crear la categoria a partir de un dict"""
        return Categoria(**d)

    @staticmethod
    def getNumInstancias():
        return Categoria.__num_instancias

    def __del__(self):
        Categoria.__num_instancias -= 1

    def __str__(self):
        return str(self.id) + " " + self.nombre

    def __repr__(self):
        return str(self)

    def __lt__(self, otro):
        return self.id < otro.id

    def __eq__(self, o):
        return self.id == o.id and self.nombre == o.nombre

    def print(self):
        print(self.id, self.nombre)

    """
    def __del__(self):
        print('Se borra: ',self.nombre)
    """


class Producto:

    def __init__(self, id=0, nombre="", cat=Categoria(), precio=0.0, exis=0):
        self.id = id
        self.nombre = nombre
        self.cat = cat
        self.precio = round(precio, 2)
        self.exis = exis

    @staticmethod
    def create(d):
        # De json a objeto
        cat = Categoria.create(d["cat"])
        return Producto(d["id"], d["nombre"], cat, d["precio"], d["exis"])

    def to_json(self):
        # De obj a formato json
        d = self.__dict__
        d["cat"] = self.cat.__dict__
        return d

    def __str__(self):
        return (
            str(self.id)
            + " "
            + self.nombre
            + " "
            + str(self.cat)
            + " "
            + str(self.precio)
            + " "
            + str(self.exis)
        )

    def __repr__(self):
        return str(self)

    def getTupla(self):
        return (self.id, self.nombre, self.cat.id, self.precio, self.exis)

    def getTupla2(self):
        return (self.nombre, self.cat.id, self.precio, self.exis, self.id)


class BaseDatos:
    """
    Implementar las operaciones CRUD: Create, Read, Delete y Update con la entidad Producto
    """

    def __init__(self, path):

        if not isfile(path):
            raise ValueError("No se encuentra el fichero: " + path)
        else:
            self.con = dbapi.connect(path)
            # print('Base de datos abierta!')

    def __getProducto(self, t):
        tcat = t[2:4]
        cat = Categoria(*tcat)
        # tprod = t[:2],cat+t[4:]
        prod = Producto(t[0], t[1], cat, t[4], t[5])
        return prod
    
    def selectCategorias(self):
        cur = None
        try:           
            cur = self.con.cursor()
            sql = "select id, nombre from categorias order by nombre"
            cur.execute(sql)
            return [Categoria(*t) for t in cur.fetchall()]

        except Exception as e:
            raise e
        finally:
            if cur:
                cur.close()

    def select(self, cat=None):
        cur = None
        try:
            cur = self.con.cursor()
            sql = """select p.id as idprod, p.nombre as producto, c.id as idcat, c.nombre as categoria,
            p.precio, p.existencias from productos p inner join categorias c
            on p.idcategoria = c.id"""
            if cat != None:
                sql += " where c.nombre=?"
                cur.execute(sql, (cat,))
            else:
                cur.execute(sql)

            return [self.__getProducto(t) for t in cur.fetchall()]

        except Exception as e:
            raise e
        finally:
            if cur:
                cur.close()

    def __ejecutar(self, sql, t):
        cur = None
        try:
            cur = self.con.cursor()
            cur.execute(sql, t)
            n = cur.rowcount
            self.con.commit()
            return n

        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            if cur:
                cur.close()

    def create(self, p):
        sql = "insert into productos(nombre, idcategoria, precio, existencias) values(?,?,?,?)"
        return self.__ejecutar(sql, p.getTupla()[1:])

    def createEmpleado(self, e):
        sql = "insert into empleados(id,nombre,cargo) values(?,?,?)"
        return self.__ejecutar(sql, e.getTupla())

    def delete(self, id):
        sql = "delete from productos where id=?"
        return self.__ejecutar(sql, (id,))

    def update(self, p):
        sql = "update productos set nombre=?, idcategoria=?, precio=?, existencias=? where id=?"
        return self.__ejecutar(sql, p.getTupla2())

    def readCategoria(self, nombre):
        """Recupera una categoria de la base de datos con el nombre"""
        cur = None
        try:
            cur = self.con.cursor()
            sql = "select id,nombre from categorias where nombre = ?"
            cur.execute(sql, (nombre,))
            t = cur.fetchone()
            if t == None:
                raise ValueError("No se encuentra la categoria: " + nombre)
            cat = Categoria(*t)
            return cat

        except Exception as e:
            raise e

        finally:
            if cur:
                cur.close()

    def read(self, id):
        cur = None
        try:
            cur = self.con.cursor()
            sql = """select p.id as idprod, p.nombre as producto, c.id as idcat, c.nombre as categoria,
            p.precio, p.existencias from productos p inner join categorias c
            on p.idcategoria = c.id
            where p.id = ?"""
            cur.execute(sql, (id,))
            t = cur.fetchone()
            if t == None:
                raise ValueError("No se encuentra el producto: " + str(id))
            else:
                return self.__getProducto(t)
        except Exception as e:
            raise e
        finally:
            if cur:
                cur.close()

    def getEmpleados(self):
        """Recuperar una lista de empleados"""
        cur = None
        try:
            cur = self.con.cursor()

            sql = "select * from empleados"
            cur.execute(sql)
            print(cur.description)
            L = []
            for t in cur.fetchall():
                L.append(Empleado(*t))
                print(t[-1])
            return L

        except Exception as e:
            raise e
        finally:
            if cur:
                cur.close()

    def __del__(self):
        if hasattr(self, "con"):
            self.con.close()
            # print('Base de datos cerrada!')


def cargarProducto():
    try:
        bd = BaseDatos(path)
        producto = bd.read(1)
        print(producto)
        print(producto.to_json())

        #p2 = bd.read(100)

    except Exception as e:
        print(e.__class__.__name__, e)


def cargaCategoria():
    try:
        bd = BaseDatos(path)
        categoria = bd.select("Bebidas")
        print(categoria)    

    except Exception as e:
        print(e.__class__.__name__, e)

def nuevoProducto():
    try:
        prod = Producto(0, "Red Bull II", Categoria(1), 2.35, 250)
        bd = BaseDatos(path)
        n = bd.create(prod)
        print('Nuevo producto: ', n)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    #cargarProducto()
    #cargaCategoria()
    nuevoProducto()