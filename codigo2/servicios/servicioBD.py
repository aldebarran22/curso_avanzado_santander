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

    def delete(self, id):
        # Abrir la base de datos
        pass

        # Ejecutar el método delete de la BD:

        # Retorna un json {"delete": ?} con el resultado del método delete de la BD:


    def get(self, id=None):
        try:            
            bd = BaseDatos(path)

            if id is None:
                # Listar todos los productos:
                L = bd.select()
                return [p.to_json() for p in L]
            
            elif id.isnumeric():
                # Localizar un solo producto por clave primaria
                prod = bd.read(id)
                return prod.to_json()
            
            else:
                # Listar productos de una categoría
                L = bd.select(id)
                return [p.to_json() for p in L]

        except Exception as e:
            abort(404, message=str(e))


api.add_resource(RecursoProducto, "/productos", "/productos/","/productos/<id>")

if __name__ == "__main__":
    app.run(debug=True)
