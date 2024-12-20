"""
Servicio de Rest con las operaciones CRUD a la BD.
"""

from flask import Flask
from flask_restful import Resource, Api, abort, request
from base_datos import BaseDatos, Categoria, Producto

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

            elif id.isnumeric():
                # Comprobar si es número entero, si lo es: cargar un producto por id
                id = int(id)
                producto = bd.read(id)
                return producto.to_json()

            else:
                # Lo tomamos como si fuera el nombre de la categoria:
                L = bd.select(id)
                return [p.to_json() for p in L]

        except Exception as e:
            abort(404, message=str(e))

    def delete(self, id):
        try:
            bd = BaseDatos(path)
            n = bd.delete(id)
            if n > 0:
                return {"delete": n}
            else:
                raise ValueError(f"No se encuentra el producto con id:{id}")

        except Exception as e:
            abort(404, menssage=str(e))

    def post(self):
        try:
            bd = BaseDatos(path)
            args = request.json

            # Tenemos que crear un objeto producto a partir del dicc en json
            producto = Producto.create(args)
            n = bd.create(producto)  # Crearlo en la BD.
            return {"create": n}

        except Exception as e:
            abort(404, message=str(e))

    def put(self):
        try:
            bd = BaseDatos(path)
            args = request.json
            print("args: ", args)

            # Tenemos que crear un objeto producto a partir del dicc en json
            producto = Producto.create(args)
            print("producto: ", producto)

            n = bd.update(producto)  # Actualizarlo en la BD.
            return {"update": n}

        except Exception as e:
            abort(404, message=str(e))


api.add_resource(RecursoProducto, "/productos", "/productos/", "/productos/<id>")

if __name__ == "__main__":
    app.run(debug=True)
