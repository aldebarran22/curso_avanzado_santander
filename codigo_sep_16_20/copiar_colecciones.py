"""
copia de colecciones mutables
"""

# Creado una ref.
L1 = [1,3,4,1,2,3]
L2 = L1
L1[0] = 1000
print('L1', L1, id(L1))
print('L2', L2, id(L2))
print()

# Una copia: de objetos inmutables ok!
L1 = [1,3,4,1,2,3]
L2 = L1.copy()
L1[0] = 1000
print('L1', L1, id(L1))
print('L2', L2, id(L2))
print()

# Una copia: con objetos mutables: 
L1 = [[1,3,4],[1,2,3]]
L2 = L1.copy()
L1[0] = 1000
L1[-1].append(999)
print('L1', L1, id(L1))
print('L2', L2, id(L2))
print()

# Copia de objetos mutables:
import copy
L1 = [[1,3,4],[1,2,3]]
L2 = copy.deepcopy(L1)
L1[0] = 1000
L1[-1].append(999)
print('L1', L1, id(L1))
print('L2', L2, id(L2))
print()
