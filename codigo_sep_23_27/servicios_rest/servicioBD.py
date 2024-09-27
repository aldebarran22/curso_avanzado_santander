"""
Servicio REST con las operaciones CRUD a la BD
"""

from flask import Flask
from flask_restful import Resource , Api, abort
from base_datos import BaseDatos, Producto, Categoria, path

app = Flask(__name__)
api = Api(app)

class RecursoBD(Resource):

    def get(self):
        try:
            bd = BaseDatos(path)
            L = bd.select()
            return [prod.to_json() for prod in L]
        
        except Exception as e:
            abort(404, str(e))

api.add_resource(RecursoBD, "/productos")

if __name__ == "__main__":
    api.run(debug=True, port=8000)