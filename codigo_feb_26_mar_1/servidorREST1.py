"""
Servidor REST implementado con Flask
"""

from flask import Flask
from flask_restful import Resource, Api

# Instanciar la aplicación:
app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


# Mapear el recurso con la petición
api.add_resource(HelloWorld, "/", "/hello")

if __name__ == "__main__":
    # Poner el servidor en marcha:
    app.run(debug=True)
