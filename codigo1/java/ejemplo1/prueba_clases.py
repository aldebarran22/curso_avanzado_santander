'''
Created on 17-dic-2024

@author: Anton
'''

from es.curso.app import Direccion, Usuario
from java.util import ArrayList
from collections import deque, Counter, namedtuple
from random import randint


if __name__ == '__main__':
    dir1 = Direccion("Gran Via", 33)
    user1 = Usuario("admin", "1234", dir1)
    user2 = Usuario("anonimo", "werT", dir1)
    user3 = Usuario("sys", "AASS", dir1)
    
    print(dir1)
    print(user1)
    
    L = [user1, user2, user3]
    for obj in L:
        print(obj)
        
    arr = ArrayList()
    arr.add(user1)
    arr.add(user2)
    arr.add(user3)
    
    print(arr)
    
    
    d = deque()
    d.append(100)
    d.append(200)
    d.appendleft(99)
    print(d)
    d.rotate(2)
    print(d)
    
    # Crear un histograma:
    L = [randint(1,20) for i in range(100)]
    c = Counter(L)
    print(c)
    
    # Tuplas con nombre:
    CuentaBancaria = namedtuple('CuentaBancaria', ['entidad','sucursal','dc','numero'], verbose=True)
    cb = CuentaBancaria(4000, 1224, 55, 12345678)
    print(cb)
    cb._replace(dc=99)
    print(cb)
    
    
    
    