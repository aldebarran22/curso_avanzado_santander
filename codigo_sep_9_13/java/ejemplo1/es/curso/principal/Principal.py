'''
Created on 12-sep-2024

@author: Anton
'''

from java.util import Random
from es.curso.clases import Direccion, Usuario


def generarNumeros():
    r = Random()
    L = list()
    
    for i in range(25):
        L.append(r.nextInt())
        
    print(L)
    
    
def testJava():
    dir = Direccion("Gran Via", 28001, 34)
    user = Usuario("Jose", 23, dir)
    print(user)
    print(user.nombre)
    

if __name__ == '__main__':
    #generarNumeros()
    testJava()
