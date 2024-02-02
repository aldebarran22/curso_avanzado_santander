"""
Ejemplo de servidor REST con la librería Flask con acceso a la BD
Operaciones CRUD:
C -> Create -> Verbo POST (un nuevo recurso)
R -> Read -> Verbo GET (recuperar un recurso)
U -> Update -> Verbo PUT (actualizar un recurso)
D -> Delete -> Verbo DELETE (eliminar un recurso)
"""

from flask import Flask
from flask_restful import Resource, Api, abort, reqparse
from base_datos import Empleado, Producto, Categoria, BaseDatos

# Creamos la aplicación y el Api
app = Flask(__name__)
api = Api(app)

path = "../../BBDD/empresa3.db"

# La categoría que va dentro del producto
parser_cat = reqparse.RequestParser()
parser_cat.add_argument("id", type=int)
parser_cat.add_argument("nombre", type=str)

# producto:
parser = reqparse.RequestParser()
parser.add_argument("id", type=int)
parser.add_argument("nombre", type=str)
parser.add_argument("cat", type=dict)
parser.add_argument("precio", type=float)
parser.add_argument("exis", type=int)


class ProductosBD(Resource):
    def get(self):
        # Recuperar todos los productos
        try:
            bd = BaseDatos(path)
            L = bd.select()
            return [p.to_json() for p in L]

        except Exception as e:
            abort(404, message=str(e))

    def delete(self, id):
        # Borrar un producto de la Base de datos con la PK (id)
        try:
            bd = BaseDatos(path)
            n = bd.delete(id)
            if n == 0:
                # No lo ha encontrado
                raise ValueError(f"El id: {id} no existe en la BD")
            else:
                return {"delete": 1}

        except Exception as e:
            abort(404, message=str(e))

    def post(self):
        try:
            args = parser.parse_args()            
            objProducto = Producto.create(args)
            bd = BaseDatos(path)
            n = bd.create(objProducto)
            return {"create": n}

        except Exception as e:
            return {"error": str(e)}


class CategoriasBD(Resource):
    def get(self, nombre):
        # Recuperar todos los productos
        try:
            bd = BaseDatos(path)
            L = bd.select(nombre)
            return [p.to_json() for p in L]

        except Exception as e:
            abort(404, message=str(e))


# Mapeo:
# GET: http://localhost:5000/productos
# GET: http://localhost:5000/productos/
# DELETE: http://localhost:5000/productos/id
api.add_resource(ProductosBD, "/productos", "/productos/", "/productos/<int:id>")

# GET: http://localhost:5000/categorias/nombre
api.add_resource(CategoriasBD, "/categorias/<string:nombre>")

if __name__ == "__main__":
    app.run(debug=True)
