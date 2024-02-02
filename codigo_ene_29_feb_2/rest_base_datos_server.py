"""
Ejemplo de servidor REST con la librería Flask con acceso a la BD
Operaciones CRUD:
C -> Create -> Verbo POST (un nuevo recurso)
R -> Read -> Verbo GET (recuperar un recurso)
U -> Update -> Verbo PUT (actualizar un recurso)
D -> Delete -> Verbo DELETE (eliminar un recurso)
"""

from flask import Flask
from flask_restful import Resource, Api, abort
from base_datos import Empleado, Producto, Categoria, BaseDatos

# Creamos la aplicación y el Api
app = Flask(__name__)
api = Api(app)

path = "../../BBDD/empresa3.db"


class ProductosBD(Resource):
    def get(self):
        # Recuperar todos los productos
        try:
            bd = BaseDatos(path)
            L = bd.select()
            return [p.to_json() for p in L]

        except Exception as e:
            abort(404, message=str(e))


# Mapeo:
api.add_resource(ProductosBD, "/productos", "/productos/")

if __name__ == "__main__":
    app.run(debug=True)
