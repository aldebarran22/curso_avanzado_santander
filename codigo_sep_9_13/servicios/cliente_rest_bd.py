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
        if fich:
            fich.close()


def testDelete(id):
    url = f"http://localhost:5000/productos/{id}"
    resp = requests.delete(url)
    print(resp.json())


def testPost():
    url = "http://localhost:5000/productos"
    prod = Producto(0, "Red Bull 2", Categoria(1), 1.6, 200)
    # Convertir el objeto a json
    dicc = prod.to_json() # un diccionario
    # Convertir el diccionario a una cadena de json
    data = json.dumps(dicc)
    # Indicar el tipo mime en las cabeceras.
    headers = {"Content-Type": "application/json"}
    resp = requests.post(url, data=data, headers=headers)
    print(resp.json())


if __name__ == "__main__":
    # testProducto(1)
    # testProductos()
    # testSaveFileProductos()
    #testDelete(83)
    testPost()
