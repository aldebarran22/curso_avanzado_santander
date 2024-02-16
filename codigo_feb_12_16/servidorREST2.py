"""
Servidor REST crud implementado con Flask
"""

from flask import Flask
from flask_restful import Resource, Api, abort
from basedatosCRUD import Empleado, BaseDatos

path = "../BBDD/empresa3.db"

# Instanciar la aplicación:
app = Flask(__name__)
api = Api(app)


class EmpleadoRecurso(Resource):
    def get(self):
        try:
            bd = BaseDatos(path)
            L = bd.select()
            return [emp.__dict__ for emp in L]

        except Exception as e:
            abort(404, str(e))


# Mapear el recurso con la petición
# GET: http://localhost:5000/empleados  --> Todos los empleados!
api.add_resource(EmpleadoRecurso, "/empleados")

if __name__ == "__main__":
    # Poner el servidor en marcha:
    app.run(debug=True)
