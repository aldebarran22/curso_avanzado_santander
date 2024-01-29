"""
Repaso de tipos en Python

Uso de funciones:
L = [1,2,3]
len(L)

L.sort()
"""

import copy

def diccionario():
    cad = "hola"
    L = [1,2,3,4]
    d = dict(zip(L, cad))
    print(d)

def copiarObjetosMutables():
    # Ojo crea una ref.
    L = [1,2,3,4]
    L2 = L
    L[0] = 1000
    print('L',L, id(L))
    print('L2', L2, id(L2))
    print()

    # Copiar pero con elementos inmutables:
    L = [1,2,3,4]
    L2 = L.copy()
    L[0] = 1000
    print('L',L, id(L))
    print('L2', L2, id(L2))
    print()

    # Copiar pero con elementos mutables:
    L = [[1,2],[3,4]]
    L2 = L.copy()
    L[0] = 1000
    L[-1].append(999)
    print('L',L, id(L))
    print('L2', L2, id(L2))
    print()

    # Copiar pero con elementos mutables OK:
    L = [[1,2],[3,4]]
    L2 = copy.deepcopy(L)
    L[0] = 1000
    L[-1].append(999)
    print('L',L, id(L))
    print('L2', L2, id(L2))
    print()


if __name__ == '__main__':
    #diccionario()
    copiarObjetosMutables()
