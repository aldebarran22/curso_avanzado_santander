"""
Implementar servidor de Rest con las 
operaciones CRUD (create, read, update, delete):
Verbos http         Operación
GET	                Read
POST	            Create
PUT	                Update
DELETE	            Delete
"""

from base_datos import Empleado, Producto, Categoria
from base_datos import BaseDatos, path

from flask import Flask
from flask_restful import Resource, Api, abort, reqparse, request

# Instanciar la aplicación:
app = Flask(__name__)
api = Api(app)

# Parsear la categoria:
parse_cat = reqparse.RequestParser()
parse_cat.add_argument("id", type=int)
parse_cat.add_argument("nombre", type=str)

# Parsear el producto:
parse_prod = reqparse.RequestParser()
parse_prod.add_argument("id", type=int)
parse_prod.add_argument("nombre", type=str)
parse_prod.add_argument("cat", type=dict)
parse_prod.add_argument("exis", type=int)
parse_prod.add_argument("precio", type=float)


class RecursoProductos(Resource):

    def post(self):
        try:
            bd = BaseDatos(path)
            args = request.json
            # args = parse_prod.parse_args()
            producto = Producto.create(args)
            n = bd.create(producto)
            return {"create": n}

        except Exception as e:
            abort(404, message=str(e))

    def delete(self, id):
        try:
            bd = BaseDatos(path)
            n = bd.delete(id)
            return {"delete": n}
        except Exception as e:
            abort(404, message=str(e))

    def get(self, id=None):
        try:
            bd = BaseDatos(path)
            if not id:
                L = bd.select()
                return [p.to_json() for p in L]
            else:
                prod = bd.read(id)
                return prod.to_json()
        except Exception as e:
            abort(404, message=str(e))


# GET: http://localhost:5000/productos
# POST: http://localhost:5000/productos
# GET: http://localhost:5000/productos/
# GET: http://localhost:5000/productos/id
api.add_resource(RecursoProductos, "/productos", "/productos/", "/productos/<int:id>")


if __name__ == "__main__":
    # Poner el servidor en marcha:
    app.run(debug=True)
