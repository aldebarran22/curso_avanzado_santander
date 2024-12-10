"""
Comparativa entre mutable (list) e inmutable (str)
"""

# mutable
L = [4,6,2,1,3,4]
print(L)
L.sort()
print(L)

#inmutable:
cad = "hola"
print(cad)
print(cad.upper()) # cad = cad.upper()
print(cad)

# Copiar objetos mutables:
L1 = [1,2,3,4,5]
L2 = L1 # Ojo es una ref.
L1[0] = 99
print("L1", L1, id(L1))
print("L2", L2, id(L2))
print()

L1 = [1,2,3,4,5]
L2 = L1.copy() # copia ok si son inmutables!
L1[0] = 99
print("L1", L1, id(L1))
print("L2", L2, id(L2))
print()

L1 = [[1,2],[3,4,5]]
L2 = L1.copy() # no copia bien si son mutables!
L1[0] = 99
L1[-1].append(99)
print("L1", L1, id(L1))
print("L2", L2, id(L2))
print()

import copy
L1 = [[1,2],[3,4,5]]
L2 = copy.deepcopy(L1) # copia bien aunque sean mutables!
L1[0] = 99
L1[-1].append(99)
print("L1", L1, id(L1))
print("L2", L2, id(L2))
print()