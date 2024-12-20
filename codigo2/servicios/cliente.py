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
    json.dump(resp.json(), fich)
    fich.close()
    print("Se ha descargado el fichero: productos.json")


if __name__ == "__main__":
    #testHelloWorld()
    testProductosGet()
