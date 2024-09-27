"""
Servicio REST con las operaciones CRUD a la BD
"""

from flask import Flask
from flask_restful import Resource , Api, abort, request
from base_datos import BaseDatos, Producto, Categoria, path

app = Flask(__name__)
api = Api(app)

class RecursoBD(Resource):

    def put(self):
        try:
            bd = BaseDatos(path) 
            args = request.json

            # Crear un objeto producto:
            producto = Producto.create(args)
            n = bd.update(producto)
            return {"update":n}

        except Exception as e:
            abort(404, message=str(e))


    def post(self):
        try:
            bd = BaseDatos(path) 
            args = request.json

            # Crear un objeto producto:
            producto = Producto.create(args)
            n = bd.create(producto)
            return {"create":n}

        except Exception as e:
            abort(404, message=str(e))


    def delete(self, param):
        try:
            bd = BaseDatos(path) 
            n = bd.delete(param)
            if n == 0:
                raise ValueError(f"No existe el id: {param}")
            else:
                return {"delete":n}
            
        except Exception as e:
            abort(404, message=str(e))

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
            
            else:
                L = bd.select(param)
                return [prod.to_json() for prod in L]
        
        except Exception as e:
            abort(404, message=str(e))

api.add_resource(RecursoBD, "/","/productos","/productos/","/productos/<param>")

if __name__ == "__main__":
    app.run(debug=True, port=8000)