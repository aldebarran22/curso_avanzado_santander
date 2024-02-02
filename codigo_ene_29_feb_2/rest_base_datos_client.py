"""
Ejemplo de peticiones GET/DELETE/PUT/POST a un servicio de REST 
con la librería requests
"""
import requests
import json

def testGET():
    rep = requests.get("http://localhost:5000/productos")
    datos = rep.json()
    #print(datos, type(datos))
    with open("productos_rest.json", "w", encoding="utf8") as f:
        json.dump(datos, f)
        print('Fichero generado ...')

def testDELETE(id):
    url = f"http://localhost:5000/productos/{id}"
    resp = requests.delete(url)
    datos = resp.json()
    print(datos)

if __name__ == "__main__":
    #testGET()
    testDELETE(10)
