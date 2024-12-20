"""
Implementación de un cliente de Rest con la librería requests
"""

import requests
import json
from base_datos import Producto, Categoria


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


def testProductosPost():
    url = "http://localhost:5000/productos"

    producto = Producto(200, "Café", Categoria(1), 1.45, 200)
    dicc = producto.to_json()
    datos = json.dumps(dicc)
    cabs = {"Content-type": "application/json"}

    resp = requests.post(url, data=datos, headers=cabs)
    print(resp.json())

def testProductosPut(id, porc = 0.15):
    # Recuperar el producto que vamos a modificar:
    url = f"http://localhost:5000/productos/{id}"

    # La petición Get:
    resp = requests.get(url)
    producto = Producto.create(resp.json())
    print(producto)

    # Modificar el precio del producto:
    producto.precio *= (1+porc)

    # Publicar de nuevo el producto -> Put
    url = "http://localhost:5000/productos"

    # Convetir de nuevo el producto a json:
    dicc = producto.to_json()
    datos = json.dumps(dicc)
    cabs = {"Content-type": "application/json"}
    resp = requests.put(url, data=datos, headers=cabs)
    print(resp.json())    

if __name__ == "__main__":
    # testHelloWorld()
    # testProductosGet()
    # testProductosGetId(1)
    # testProductosGetCategoria("bebidas")
    # testProductosDeleteId(26)
    testProductosPost()
