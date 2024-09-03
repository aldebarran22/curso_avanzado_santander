"""
Pruebas con tuplas
"""

def funcion(a,b):
    return a+b

def sumaResta(a,b):
    return a+b, a-b

L = [(1,2),(3,4),(5,6)]
for i,j in L:
    print(funcion(i,j))

for t in L:
    print(funcion(*t))

a, b = 1,2
a,b = b,a
print(a,b)

s,r = sumaResta(a,b)
print(s,r)

d = {"a":1, "b":2}
print(funcion(**d))

