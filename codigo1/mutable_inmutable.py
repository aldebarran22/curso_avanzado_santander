"""
Comparativa entre un tipo mutable e inmutable
"""

# Objeto mutable:
L = [3,5,6,2,1,3,7]
print(L)
L.sort()
print(L)

# Objeto inmutable:
cad = "hola"
print(cad)
print(cad.upper())
print(cad)

# Copia de objetos mutables:
L1 = [3,4,5,2,1]
L2 = L1 # ojo, es una referencia.
L1[0] = 99
print("L1", L1, id(L1))
print("L2", L2, id(L2))
print()

L1 = [3,4,5,2,1]
L2 = L1.copy() # ojo, es una referencia.
L1[0] = 99
print("L1", L1, id(L1))
print("L2", L2, id(L2))

print()

L1 = [[3,4],[5,2,1]]
L2 = L1.copy() # ojo, es una copia superficial.
L1[0] = 99
L1[-1].append(999)
print("L1", L1, id(L1))
print("L2", L2, id(L2))


print()

import copy
L1 = [[3,4],[5,2,1]]
L2 = copy.deepcopy(L1) # es una copia profunda
L1[0] = 99
L1[-1].append(999)
print("L1", L1, id(L1))
print("L2", L2, id(L2))
