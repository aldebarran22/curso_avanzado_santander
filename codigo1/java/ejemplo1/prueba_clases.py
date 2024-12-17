'''
Created on 17-dic-2024

@author: Anton
'''

from es.curso.app import Direccion, Usuario
from java.util import ArrayList

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
    
    