"""
Ejemplo de servidor REST con la librería Flask
"""

from flask import Flask
from flask_restful import Resource, Api

# Creamos la aplicación y el Api
app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


# Mapear el recurso con una URL:
api.add_resource(HelloWorld, "/")

if __name__ == "__main__":
    # Poner en marcha el servidor:
    app.run(debug=True)
