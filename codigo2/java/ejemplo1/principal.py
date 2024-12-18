'''
Created on 18-dic-2024

@author: Anton
'''

from java.util import ArrayList
from es.curso.clases import Usuario, Direccion

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