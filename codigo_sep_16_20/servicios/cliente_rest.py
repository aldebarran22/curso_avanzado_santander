"""
Cliente REST con la librería requests
"""

import requests
import json


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

def testDelete():
    url = "http://localhost:5000/productos/3"
    resp = requests.get(url)
    print(resp.json())

if __name__ == "__main__":
    testDelete()
