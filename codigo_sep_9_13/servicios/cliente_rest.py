"""
Cliente REST. Petición GET con la librería requests
"""

import requests

resp = requests.get("http://localhost:5000")
print(resp.text)
d = resp.json()
print(d, type(d))
