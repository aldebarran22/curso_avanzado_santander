'''
Created on 15-feb-2024

@author: Anton
'''

#!/usr/bin/python
# -*- coding: latin-1 -*-

from es.curso.clases import Usuario

if __name__ == '__main__':
    user = Usuario("Jose","Sanz",45)
    print(user)
    
    L = [user, Usuario("Ana","Perez",36), Usuario("Andres","Gomez",56)]
    for i in L:
        print(i)
        
    print(type(L))