"""
Ejemplo de peticiones GET/DELETE/PUT/POST a un servicio de REST 
con la librería requests
"""
import requests
import json
from base_datos import Categoria, Producto


def testGET():
    rep = requests.get("http://localhost:5000/productos")
    datos = rep.json()
    # print(datos, type(datos))
    with open("productos_rest.json", "w", encoding="utf8") as f:
        json.dump(datos, f)
        print("Fichero generado ...")


def testDELETE(id):
    url = f"http://localhost:5000/productos/{id}"
    resp = requests.delete(url)
    datos = resp.json()
    print(datos)


def testPOST():
    url = "http://localhost:5000/productos/"
    cat = Categoria(1, "Bebidas")
    prod = Producto(100, "CocaCola3", cat, 1.8, 100)
    headers = {"Content-Type": "application/json"}
    resp = requests.post(url, headers=headers, data=json.dumps(prod.to_json()))
    print(resp.json())


if __name__ == "__main__":
    # testGET()
    # testDELETE(10)
    testPOST()
