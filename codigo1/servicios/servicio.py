"""
Implementar un servicio con Flask.
Ejemplo: Hello World
"""

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):

    def get(self):
        return {"hello": "world"}


# Mapeamos el recurso con una URI:
# Cuando se detecta una petición / se instancia el recurso
# y según el verbo Rest se lanza un método de la clase del
# recurso
api.add_resource(HelloWorld, "/")

# Para poner en marcha el Servidor:
if __name__ == "__main__":
    app.run(debug=True)  # http://localhost:5000
