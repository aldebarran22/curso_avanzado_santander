"""
Servidor REST + Base de datos
"""

from base_datos import BaseDatos, Categoria, Producto, path
from flask import Flask
from flask_restful import Resource, Api, abort, request

app = Flask(__name__)
api = Api(app)

class RecursoProducto(Resource):

    def get(self, id=None):
        try:
            bd = BaseDatos(path)
            if not id:
                # Devolver todos los productos:
                L = bd.select()
                return [p.to_json() for p in L]
            else:
                # Devolver un producto concreto:
                prod = bd.read(id)
                return prod.to_json()
            
        except Exception as e:
            abort(404, message=str(e))

    def delete(self, id):
        try:
            bd = BaseDatos(path)
            n = bd.delete(id)
            return {"delete":n}        

        except Exception as e:
            abort(404, message=str(e))

    def post(self):
        try:
            bd = BaseDatos(path)
            # Recuperamos los parámetros de la petición
            # en formato json
            args = request.json

            # Crear el objeto producto a partir del diccionario
            producto = Producto.create(args)
            n = bd.create(producto)
            return {"create", n}
        
        except Exception as e:
            abort(404, message=str(e))


# Definir el mapeo entre el recurso y la petición:
# Tipos de peticiones que atiende este recurso:
# http://localhost:5000/productos -> listar todos
# http://localhost:5000/productos/ -> listar todos
# http://localhost:5000/productos/id -> un producto (id)
api.add_resource(RecursoProducto, "/productos", "/productos/","/productos/<int:id>")

if __name__=='__main__':
    app.run(debug=True)


