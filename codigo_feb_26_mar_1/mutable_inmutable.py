"""
Comparativa entre un tipo mutable / inmutable
"""

def prueba1():
    # mutable
    L = [1, 2, 3, 4, 5, -7,0,4]
    L.sort()
    print(L)

    # inmutables
    cad = "hola"
    print(cad.upper())
    print(cad)

def copiaListas():
    L1 = [3,5,6,3,1,2]
    L2 = L1 # Crea una ref
    L1[0] = 1000
    print('L1',L1, id(L1))
    print('L2',L2, id(L2))
    print('-'*20)

    # Copiar una lista de objetos inmutables
    L1 = [3,5,6,3,1,2]
    L2 = L1.copy()
    L1[0] = 1000
    print('L1',L1, id(L1))
    print('L2',L2, id(L2))
    print('-'*20)
    
    # Copiar una lista de objetos mutables
    L1 = [[3,5,6],[3,1,2]]
    L2 = L1.copy()
    L1[0] = 1000
    L1[-1].append(999)
    print('L1',L1, id(L1))
    print('L2',L2, id(L2))
    print('-'*20)

    # Copia profunda de objetos:
    import copy
    L1 = [[3,5,6],[3,1,2]]
    L2 = copy.deepcopy(L1)
    L1[0] = 1000
    L1[-1].append(999)
    print('L1',L1, id(L1))
    print('L2',L2, id(L2))
    print('-'*20)


if __name__ == '__main__':
    copiaListas()