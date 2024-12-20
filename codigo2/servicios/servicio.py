"""
Ejemplo de publicación de un servicio de Rest con Flask
"""

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Recurso(Resource):

    def get(self):
        return {"hello":"world"}
    
# Mapear la URL al Recurso
api.add_resource(Recurso, "/")

if __name__ == "__main__":
    # Arrancar el servidor
    app.run(debug=True)