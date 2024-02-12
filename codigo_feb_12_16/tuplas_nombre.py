"""
Tuplas con nombre: 
CuentaBancaria: entidad, sucursal, dc, numero
"""

from collections import namedtuple

CuentaBancaria = namedtuple("CuentaBancaria", ["entidad", "sucursal", "dc", "numero"])
cb = CuentaBancaria(2000, 1234, 99, 12345678)
print(cb)
