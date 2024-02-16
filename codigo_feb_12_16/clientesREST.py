"""
Consumir servicios REST con la librería requests
"""
from requests import get

def testHello():
    url = "http://localhost:5000"
    resp = get(url)
    print(resp.json())

def testEmpleados():
    url = "http://localhost:5000/empleados"
    resp = get(url)
    print(resp.json())


if __name__ == '__main__':
    #testHello()
    testEmpleados()