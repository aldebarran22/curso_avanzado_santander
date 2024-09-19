'''
Created on 19-sep-2024

@author: Anton
'''

from java.lang import String
from java.util import ArrayList
from es.curso.clases_java import Permisos, Usuario

def prueba1():
    nombre = String("Nombre Apellidos")
    print(nombre)
    
    L = [1,2,3,4,5]
    L.append(10)
    print(L)
    
    arr = ArrayList()
    arr.add(45)
    arr.add(99)
    arr.add(10)
    print(arr)
    
def prueba2():
    p1 = Permisos('W', 'documento PDF');
    p2 = Permisos('X', 'web');
    
    permisos = ArrayList()
    permisos.add(p1)
    permisos.add(p2)
    print(permisos)
    
    user = Usuario("Nombre de usuario", "administrador","123455", permisos)
    print(user)

if __name__ == '__main__':    
    # prueba1()
    prueba2()    
    