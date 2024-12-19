"""
Implementación de un cliente Rest con la librería
requests.
"""

from requests import get, delete
import json


def testHelloWorld():
    url = "http://localhost:5000"
    resp = get(url)
    print(resp.json())


def testGetProductos():
    url = "http://localhost:5000/productos"
    resp = get(url)
    fich = open("productos.json", "w")
    json.dump(resp.json(), fich, indent=4)
    fich.close()
    print("Se ha generado el fichero de productos...")


def testDeleteProductos(id):
    url = f"http://localhost:5000/productos/{id}"
    resp = delete(url)
    print(resp.json())


if __name__ == "__main__":
    # testHelloWorld()
    # testGetProductos()
    testDeleteProductos(24)
