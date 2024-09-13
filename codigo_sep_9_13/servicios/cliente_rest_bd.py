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

def testPut(id):
    try:
        url = f"http://localhost:5000/productos/{id}"
        resp = requests.get(url)
        dicc = resp.json()
        print('dicc: ', dicc)
        obj = Producto.create(dicc)
        print('obj: ', obj)
        obj.exis = 500
        obj.precio = 2.5
        dicc = obj.to_json()  # un diccionario
        # Convertir el diccionario a una cadena de json
        data = json.dumps(dicc)

        print("\nData: ", data)

        # Indicar el tipo mime en las cabeceras.
        url = "http://localhost:5000/productos"
        headers = {"Content-Type": "application/json"}
        resp = requests.put(url, data=data, headers=headers)
        print(resp.text)
        
    except Exception as e:
        print(e)




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
    try:
        url = "http://localhost:5000/productos"
        prod = Producto(0, "Red Bull 100", Categoria(1, "bebidas"), 1.6, 200)
        # Convertir el objeto a json
        dicc = prod.to_json()  # un diccionario
        # Convertir el diccionario a una cadena de json
        data = json.dumps(dicc)

        print("\nData: ", data)

        # Indicar el tipo mime en las cabeceras.
        headers = {"Content-Type": "application/json"}
        resp = requests.post(url, data=data, headers=headers)
        print(resp.text)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # testProducto(1)
    # testProductos()
    # testSaveFileProductos()
    # testDelete(83)
    #testPost()
    testPut(90)
