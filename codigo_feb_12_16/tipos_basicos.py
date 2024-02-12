"""
Tipos básicos
"""
import copy

def tiposNumericos():
    resul = 23 + 6.88 + 6 + 2j
    print(resul, type(resul))

    # False: 0, "", [], None


def copiaListas():
    # Crear referencias:
    L1 = [1, 2, 3, 4, 5]
    L2 = L1
    L1[0] = 1000
    print("L1", L1, id(L1))
    print("L2", L2, id(L2))
    print()

    #Copia: ojo funciona bien si tenemos elementos inmutables:
    L1 = [1, 2, 3, 4, 5]
    L2 = L1.copy()
    L1[0] = 1000
    print("L1", L1, id(L1))
    print("L2", L2, id(L2))
    print()

    # Copia de listas con elementos mutables: MAL
    L1 = [[1, 2], [3, 4, 5]] # Elementos compartidos!
    L2 = L1.copy()
    L1[0] = 1000
    L1[-1].append(999)
    print("L1", L1, id(L1))
    print("L2", L2, id(L2))
    print()

    # Copia de listas con elementos mutables: copia profunda    
    L1 = [[1, 2], [3, 4, 5]]
    L2 = copy.deepcopy(L1)
    L1[0] = 1000
    L1[-1].append(999)
    print("L1", L1, id(L1))
    print("L2", L2, id(L2))
    print()


if __name__ == "__main__":
    # tiposNumericos()
    copiaListas()
