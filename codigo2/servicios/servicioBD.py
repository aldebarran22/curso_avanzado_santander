"""
Implementar un servicio Rest  para implementar las operaciones
CRUD sobre un producto:
- C : Create -> post
- R : Read -> get
- U : Update -> put
- D : delete -> delete
"""

from flask import Flask
from flask_restful import Resource, Api, abort
from base_datos import Categoria, Producto, BaseDatos

app = Flask(__name__)
api = Api(app)
path = "empresa3.db"


class RecursoProducto(Resource):

    def get(self, id=None):
        try:            
            bd = BaseDatos(path)

            if id is None:
                # Listar todos los productos:
                L = bd.select()
                return [p.to_json() for p in L]
            
            else:
                prod = bd.read(id)
                return prod.to_json()

        except Exception as e:
            abort(404, message=str(e))


api.add_resource(RecursoProducto, "/productos", "/productos/","/productos/<id>")

if __name__ == "__main__":
    app.run(debug=True)
