"""
Servicio REST con las operaciones CRUD a la BD
"""

from flask import Flask
from flask_restful import Resource , Api, abort
from base_datos import BaseDatos, Producto, Categoria, path

app = Flask(__name__)
api = Api(app)

class RecursoBD(Resource):

    def get(self, param=None):
        try:
            bd = BaseDatos(path)
            if param is None:
                L = bd.select()
                return [prod.to_json() for prod in L]
            
            elif param.isnumeric():
                id = int(param)
                prod = bd.read(id)
                return prod.to_json()
        
        except Exception as e:
            abort(404, str(e))

api.add_resource(RecursoBD, "/productos","/productos/<param>")

if __name__ == "__main__":
    app.run(debug=True, port=8000)