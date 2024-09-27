"""
Cliente REST implementado con requests.
"""

import requests
import json


def testHW():
    url = "http://localhost:8000"
    resp = requests.get(url)
    print("RESP: ", resp.json())


def descargarJSON():
    fich = None
    try:
        url = "http://localhost:8000/productos"
        resp = requests.get(url)

        fich = open("productos.json", "w")
        json.dump(resp.json(), fich)
        print("productos.json grabado!!")

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    # testHW()
    descargarJSON()
