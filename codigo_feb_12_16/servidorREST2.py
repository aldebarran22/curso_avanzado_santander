"""
Servidor REST crud implementado con Flask
"""

from flask import Flask
from flask_restful import Resource, Api, abort, reqparse
from basedatosCRUD import Empleado, BaseDatos

path = "../BBDD/empresa3.db"

# Parseador de los parámetros de un empleado:
parser = reqparse.RequestParser()
parser.add_argument("id", type=int)
parser.add_argument("nombre", type=str)
parser.add_argument("cargo", type=str)

# Instanciar la aplicación:
app = Flask(__name__)
api = Api(app)


class EmpleadoListRecurso(Resource):
    def get(self):
        try:
            bd = BaseDatos(path)
            L = bd.select()
            return [emp.__dict__ for emp in L]

        except Exception as e:
            abort(404, str(e))

    def post(self):
        # Crear un empleado en la BD:
        try:
            bd = BaseDatos(path)
            args = parser.parse_args()
            empleado = Empleado(args["id"], args["nombre"], args["cargo"])
            n = bd.create(empleado)
            return {"create": n}

        except Exception as e:
            return {"error": str(e)}


class EmpleadoResource(Resource):

    def get(self, id):
        try:
            bd = BaseDatos(path)
            emp = bd.read(id)
            return emp.__dict__

        except ValueError as e:
            abort(404, message=str(e))


# Mapear el recurso con la petición
# GET: http://localhost:5000/empleados  --> Todos los empleados!
api.add_resource(EmpleadoListRecurso, "/empleados")
# GET: http://localhost:5000/empleados/id
api.add_resource(EmpleadoResource, "/empleados/<int:id>")

if __name__ == "__main__":
    # Poner el servidor en marcha:
    app.run(debug=True)
