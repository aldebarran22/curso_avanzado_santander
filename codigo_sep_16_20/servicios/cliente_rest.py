"""
Cliente REST con la librería requests
"""

import requests
import json
from base_datos import Categoria, Producto

def testHW():
    url = "http://localhost:5000"
    resp = requests.get(url)
    print(resp.json())


def testProductos():
    fich = None
    try:
        url = "http://localhost:5000/productos"
        resp = requests.get(url)
        dicc = resp.json()

        fich = open("productos.json", "w")
        json.dump(dicc, fich, indent=4)
        print("Fichero generado ...")

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


def testDelete(id):
    url = f"http://localhost:5000/productos/{id}"
    resp = requests.delete(url)
    print(resp.json())

def testPost():
    url = "http://localhost:5000/productos"
    prod = Producto(0, "CocaCola22", Categoria(1), 2.5, 1000)
    dicc = prod.to_json()

    cad = json.dumps(dicc)
    headers = {"Content-type":"application/json"}
    resp = requests.post(url, data=cad, headers=headers)
    print(resp.json())

def testPut(id, precio, existencias):
    try:
        url = f"http://localhost:5000/productos/{id}"
        resp = requests.get(url)
        dicc = resp.json()

        producto = Producto.create(dicc)
        producto.precio = precio
        producto.exis = existencias

        dicc = producto.to_json()
        cad = json.dumps(dicc)
        headers = {"Content-type":"application/json"}
        url = "http://localhost:5000/productos"
        resp = requests.put(url, data=cad, headers=headers)
        print(resp.json())


    except Exception as e:
        print(e)


if __name__ == "__main__":
    testPut(101, 1.05, 500)
