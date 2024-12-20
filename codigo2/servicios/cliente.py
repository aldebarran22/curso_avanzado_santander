"""
Implementación de un cliente de Rest con la librería requests
"""

import requests
import json


def testHelloWorld():
    url = "http://localhost:5000"
    resp = requests.get(url)
    print(resp.json())


def testProductosGet():
    url = "http://localhost:5000/productos"
    resp = requests.get(url)
    fich = open("productos.json", "w")
    json.dump(resp.json(), fich, indent=4)
    fich.close()
    print("Se ha descargado el fichero: productos.json")


def testProductosGetId(id):
    url = f"http://localhost:5000/productos/{id}"
    resp = requests.get(url)
    print(resp.json())


def testProductosGetCategoria(categoria):
    url = f"http://localhost:5000/productos/{categoria}"
    resp = requests.get(url)
    print(resp.json())

def testProductosDeleteId(id):
    url = f"http://localhost:5000/productos/{id}"
    resp = requests.delete(url)
    print(resp.json())


if __name__ == "__main__":
    # testHelloWorld()
    # testProductosGet()
    # testProductosGetId(1)
    # testProductosGetCategoria("bebidas")
    testProductosDeleteId(26)
