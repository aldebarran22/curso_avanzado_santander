"""
Ejemplo de servidor REST con la librería Flask con acceso a la BD
Operaciones CRUD:
C -> Create -> Verbo POST (un nuevo recurso)
R -> Read -> Verbo GET (recuperar un recurso)
U -> Update -> Verbo PUT (actualizar un recurso)
D -> Delete -> Verbo DELETE (eliminar un recurso)
"""

from flask import Flask
from flask_restful import Resource, Api
from base_datos import Empleado, Producto, Categoria, BaseDatos

# Creamos la aplicación y el Api
app = Flask(__name__)
api = Api(app)


class ProductosBD(Resource):
    def get(self):
        # Recuperar todos los productos
        try:
            pass
        except Exception as e:
            pass


# Mapeo:
api.add_resource(ProductosBD, "/productos", "/productos/")

if __name__ == "__main__":
    app.run(debug=True)
