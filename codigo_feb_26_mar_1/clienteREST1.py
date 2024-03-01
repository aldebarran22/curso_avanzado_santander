"""
Consumir un servicio de REST con la lib: requests
"""

from requests import get


def testServicioHello():
    url = "http://localhost:5000/hello"
    resp = get(url).json()
    print(resp)


def testListaProductos():
    url = "http://localhost:5000/productos"
    resp = get(url).json()
    print(resp)

def testReadProducto(id):
    url = f"http://localhost:5000/productos/{id}"
    resp = get(url).json()
    print(resp)

if __name__ == "__main__":
    # testServicioHello()
    # testListaProductos()
    testReadProducto(12)
