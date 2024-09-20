"""
Cliente REST con la librería requests
"""

import requests

def testHW():
    url = "http://localhost:5000"
    resp = requests.get(url)
    print(resp.json())

if __name__ == '__main__':
    testHW()