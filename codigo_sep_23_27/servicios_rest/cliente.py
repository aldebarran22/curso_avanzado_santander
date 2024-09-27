"""
Cliente REST implementado con requests.
"""

import requests

def testHW():
    url = "http://localhost:8000"
    resp = requests.get(url)
    print("RESP: ", resp.json())

if __name__ == '__main__':
    testHW()