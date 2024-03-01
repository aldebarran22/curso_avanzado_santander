"""
Consumir un servicio de REST con la lib: requests
"""

from requests import get, delete, post
from base_datos import Categoria, Producto
import json


def testServicioHello():
    url = "http://localhost:5000/hello"
    resp = get(url).json()
    print(resp)


def testListaProductos():
    url = "http://localhost:5000/productos"
    resp = get(url).json()
    print(resp)


def testReadProducto(id):
    url = f"http://localhost:5000/productos/{id}"
    resp = get(url).json()
    print(resp)


def testDeleteProducto(id):
    url = f"http://localhost:5000/productos/{id}"
    resp = delete(url).json()
    print(resp)


def testCreateProducto():
    cat = Categoria(1, None)
    prod = Producto(0, "Red Bull3", cat, 1.6, 100)
    dicc = prod.to_json()
    url = "http://localhost:5000/productos"
    data = json.dumps(dicc)
    headers = {"Content-Type": "application/json"}
    resp = post(url, headers=headers, data=data)
    print(resp.json())


if __name__ == "__main__":
    # testServicioHello()
    # testListaProductos()
    # testReadProducto(12)
    # testDeleteProducto(12)
    testCreateProducto()
