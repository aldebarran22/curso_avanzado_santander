"""
Cliente REST + base de datos
"""

from base_datos import Producto, Categoria
import requests
import json

def testProductos():
    url = "http://localhost:5000/productos"
    resp = requests.get(url)
    print(resp.json())

def testProducto(id):
    url = f"http://localhost:5000/productos/{id}"
    resp = requests.get(url)
    print(resp.json())

def testSaveFileProductos():
    fich = None
    try:
        url = "http://localhost:5000/productos"
        resp = requests.get(url)
        dicc = resp.json()

        fich = open("productos.json", "w")
        json.dump(dicc, fich, indent=4)

    except Exception as e:
        print(e)
    finally:
        if fich: fich.close()

if __name__ == '__main__':
    #testProducto(1)
    #testProductos()
    testSaveFileProductos()