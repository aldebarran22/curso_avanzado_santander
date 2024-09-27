"""
Cliente REST implementado con requests.
"""

import requests
import json
from base_datos import Producto, Categoria


def testHW():
    url = "http://localhost:8000"
    resp = requests.get(url)
    print("RESP: ", resp.json())


def testDelete(id):
    url = f"http://localhost:8000/productos/{id}"
    resp = requests.delete(url)
    print("RESP: ", resp.json())


def descargarJSON():
    fich = None
    try:
        url = "http://localhost:8000/productos"
        resp = requests.get(url)

        fich = open("productos.json", "w")
        json.dump(resp.json(), fich, indent=4)
        print("productos.json grabado!!")

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


def nuevoProducto():
    url = "http://localhost:8000/productos"
    p = Producto(0, "Redbull 33", Categoria(1), 1.75, 200)
    dicc = p.to_json()

    cad = json.dumps(dicc)
    headers = {"Content-type": "application/json"}
    resp = requests.post(url, data=cad, headers=headers)
    print(resp.json())


def actualizarProducto(id, precio=0, exis=0):
    url = f"http://localhost:8000/productos/{id}"
    resp = requests.get(url)
    prod = Producto.create(resp.json())
    print(prod)
    prod.precio = precio
    prod.exis = exis
    print(prod)
    url = "http://localhost:8000/productos"
    dicc = prod.to_json()
    cad = json.dumps(dicc)
    headers = {"Content-type": "application/json"}
    resp = requests.put(url, data=cad, headers=headers)
    print(resp.json())


if __name__ == "__main__":
    # testHW()
    # descargarJSON()
    # testDelete(24)
    # nuevoProducto()
    actualizarProducto(precio=5.0, exis=4000)
