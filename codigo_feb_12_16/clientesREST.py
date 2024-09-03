"""
Consumir servicios REST con la librería requests
"""

from requests import get, post
from basedatosCRUD import Empleado
import json


def testHello():
    url = "http://localhost:5000"
    resp = get(url)
    print(resp.json())


def testEmpleados():
    url = "http://localhost:5000/empleados"
    resp = get(url)
    print(resp.json())


def crearEmpleado():
    url = "http://localhost:5000/empleados"
    emp = Empleado(0, "Jose Julio", "Gerente")
    headers = {"Content-Type": "application/json"}
    datos = json.dumps(emp.__dict__)
    resp = post(url, headers=headers, data=datos)
    print("post empleado: ", resp.json())


if __name__ == "__main__":
    # testHello()
    # testEmpleados()
    crearEmpleado()
