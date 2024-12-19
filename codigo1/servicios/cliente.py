"""
Implementación de un cliente Rest con la librería
requests.
"""

from requests import get

def testHelloWorld():
    url = "http://localhost:5000"
    resp = get(url)
    print(resp.json())


if __name__ == '__main__':
    testHelloWorld()