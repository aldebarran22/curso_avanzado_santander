"""
Ejemplo de petición GET a un servicio de REST con la librería 
requests
"""
import requests

if __name__ == "__main__":
    rep = requests.get("http://localhost:5000")
    datos = rep.json()
    print(datos, type(datos))
