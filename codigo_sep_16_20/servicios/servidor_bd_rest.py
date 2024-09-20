"""
Servidor REST con la BD
"""

from base_datos import BaseDatos, path, Categoria, Producto
from flask import Flask
from flask_restful import Resource, Api, abort, request

app = Flask(__name__)
api = Api(app)


class Servidor(Resource):

    def put(self):
        try:
            bd = BaseDatos(path)
            args = request.json

            producto = Producto.create(args)
            print(producto)
            n = bd.update(producto)
            return {"update":n}
        
        except Exception as e:
            abort(404, message=str(e))


    def post(self):
        try:
            bd = BaseDatos(path)
            args = request.json

            producto = Producto.create(args)
            print(producto)
            n = bd.create(producto)
            return {"create":n}
        
        except Exception as e:
            abort(404, message=str(e))

    def delete(self,id):
        try:
            bd = BaseDatos(path) 
            n = bd.delete(id)
            if n == 0:
                raise ValueError(f"No se encuentra el id: {id}")
            else:
                return {"delete":n}
        
        except Exception as e:
            abort(404, message=str(e))

    def get(self, id=None):
        try:
            bd = BaseDatos(path)
            if id is None:
                # Recuperamos todos los productos:
                L = bd.select()
                return [p.to_json() for p in L]

            elif id.isnumeric():
                prod = bd.read(int(id))
                return prod.to_json()

            else:
                ids = [int(i) for i in id.split(",")]
                resul = []
                for i in ids:
                    obj = bd.read(i)
                    resul.append(obj.to_json())

                return resul

        except Exception as e:
            abort(404, message=str(e))


api.add_resource(Servidor, "/productos", "/productos/<id>")

if __name__ == "__main__":
    app.run(debug=True)  # Petición : http://localhost:5000
