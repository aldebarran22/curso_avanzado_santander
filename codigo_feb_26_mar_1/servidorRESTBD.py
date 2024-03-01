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
from flask_restful import Resource, Api, abort

# Instanciar la aplicación:
app = Flask(__name__)
api = Api(app)


class RecursoProductos(Resource):

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
# GET: http://localhost:5000/productos/
# GET: http://localhost:5000/productos/id
api.add_resource(RecursoProductos, "/productos", "/productos/", "/productos/<int:id>")


if __name__ == "__main__":
    # Poner el servidor en marcha:
    app.run(debug=True)
