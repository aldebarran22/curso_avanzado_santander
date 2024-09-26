'''
Created on 26-sep-2024

@author: Anton
'''

from java.util import ArrayList
from es.curso.ejemplo_java import Permiso, Usuario

def pruebaArrayList():
    arr = ArrayList()
    
    for i in range(50):
        arr.add(i)
    
    print(arr[:5])
    
def pruebaClasesJava():
    p1 = Permiso("fichero.xlsx", 'x')
    p2 = Permiso("apuntes.pdf", 'r')
    
    user = Usuario("invitado", "1234")
    user.addPermiso(p1)
    user.addPermiso(p2)
    
    print(user)
    

if __name__ == '__main__':
    # pruebaArrayList()
    pruebaClasesJava()