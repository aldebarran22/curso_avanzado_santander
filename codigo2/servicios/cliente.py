"""
Implementación de un cliente de Rest con la librería requests
"""

import requests


def testHelloWorld():
    url = "http://localhost:5000"
    resp = requests.get(url)
    print(resp.json())

if __name__ == '__main__':
    testHelloWorld()