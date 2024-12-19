"""
Servicio de Rest con las operaciones CRUD a la BD.
"""

from flask import Flask
from flask_restful import Resource, Api, abort
from base_datos import BaseDatos, Categoria, Producto

app = Flask(__name__)
api = Api(app)
path = "empresa3.db"


class RecursoProducto(Resource):

    def get(self, id):
        try:
            bd = BaseDatos(path)
            producto = bd.read(id)
            return producto.to_json()

        except Exception as e:
            abort(404, message=str(e))


api.add_resource(RecursoProducto, "productos/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)
