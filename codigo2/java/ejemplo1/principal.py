'''
Created on 18-dic-2024

@author: Anton
'''

from java.util import ArrayList
from es.curso.clases import Usuario, Direccion
from collections import deque, defaultdict, namedtuple, Counter
from random import randint

class User:
    
    def __init__(self, login="", passw=""):
        self.login = login
        self.passw = passw
        
    def __str__(self):
        return self.login + " " + self.passw
    
    def __repr__(self):
        return str(self)
    

if __name__ == '__main__':
    arr = ArrayList()
    arr.add(User("admin","1232"))
    arr.add(User("anonimo","hola"))
    print(arr)
    
    direccion = Direccion("Gran Via", 77)
    user1 = Usuario("Jose", 34, direccion)
    user2 = Usuario("Gema", 39, direccion)
    
    L = [user1, user2]
    print(L)
    
    # Ejemplo con deque:
    d = deque()
    d.append(10)
    d.appendleft(-10)
    d.extend((12,3,4,5,6))
    print(d)
    d.rotate(3)
    print(d)
    
    # Ejemplo con defaultdict
    L = [randint(1,20) for _ in range(400)]
    c = Counter(L)
    print(c)
    
    
    