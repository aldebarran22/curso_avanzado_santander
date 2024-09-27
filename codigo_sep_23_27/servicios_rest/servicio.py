"""
Servicio REST con Flask.
"""

from flask import Flask
from flask_restful import Resource , Api

app = Flask(__name__)
api = Api(app)

# Definir un recurso con las operaciones HTTP (Verbos REST)
class HelloWorld(Resource):

    def get(self):
        return {"hello ": "world"}

# Mapear un recurso a una petición
api.add_resource(HelloWorld, "/")

if __name__=="__main__":
    app.run(debug =True) #