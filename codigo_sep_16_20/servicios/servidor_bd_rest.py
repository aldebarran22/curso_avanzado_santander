"""
Servidor REST con la BD
"""

from base_datos import BaseDatos, path, Categoria, Producto
from flask import Flask
from flask_restful import Resource , Api, abort

app = Flask(__name__)
api = Api(app)

class Servidor(Resource):

    def get(self, id=None):        
        try:
            bd = BaseDatos(path)
            if id is None:
                # Recuperamos todos los productos:
                L = bd.select()
                return [p.to_json() for p in L]
            else:
                prod = bd.read(id)
                return prod.to_json()

        except Exception as e:
            abort(404, message=str(e))
    
api.add_resource(Servidor ,"/productos","/productos/<int:id>")

if __name__=="__main__":
    app.run(debug =True) # Petición : http://localhost:5000