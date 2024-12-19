"""
Implementación de un cliente Rest con la librería
requests.
"""

from requests import get, delete, post, put
import json
from base_datos import Categoria, Producto


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

def testPostProductos():
    url = "http://localhost:5000/productos"

    # Crear un objeto producto:
    nuevo = Producto(150, "Red Bull 3", Categoria(1), 1.77, 100)
    dicc = nuevo.to_json()
    cabs = {"Content-type": "application/json"}
    resp = post(url, data=json.dumps(dicc), headers=cabs)
    print(resp.json())
     

if __name__ == "__main__":
    # testHelloWorld()
    # testGetProductos()
    # testDeleteProductos(24)
    testPostProductos()
