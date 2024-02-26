"""
Pruebas con tuplas
"""

def funcion(a,b):
    return a+b


L = [(1,2),(3,4),(5,6)]
for i,j in L:
    print(funcion(i,j))

for t in L:
    print(funcion(*t))