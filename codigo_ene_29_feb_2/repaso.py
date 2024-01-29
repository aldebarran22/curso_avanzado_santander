"""
Repaso de tipos en Python

Uso de funciones:
L = [1,2,3]
len(L)

L.sort()
"""

import copy
from random import randint

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

def slicing():
    # Se aplica a list, str y tuple
    # L[ini:fin-1:salto=1]
    L = [1,3,4,5,6,7]
    print('los 3 primeros: ', L[0:3], L[:3])
    print('los 3 últimos: ', L[-3:])
    print('quitar primero y último: ',L[1:-1])
    print('la lista de dos en dos: ', L[::2])
    print('invertida: ', L[::-1])
    # numba para optimizar

def listcomp():
    # Generar una lista de las potencias de dos:
    L = [2**i for i in range(0,11)]
    print(L)

    # Generar 20 aleatorios:
    L2 = [randint(10,50) for _ in range(20)]
    print(L2)

    # Filtrar multiplos de 3:
    L3 = [i for i in L2 if i % 3 == 0]
    print(L3)

if __name__ == '__main__':
    #diccionario()
    #copiarObjetosMutables()
    #slicing()
    listcomp()
