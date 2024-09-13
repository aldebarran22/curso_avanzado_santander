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

if __name__ == '__main__':
    testProducto(1)