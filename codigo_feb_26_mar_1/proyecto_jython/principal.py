'''
Created on 29-feb-2024

@author: Anton
'''

from java.util import  ArrayList
from random import randint
from java.lang import String


if __name__ == '__main__':
    L = [randint(1,50) for _ in range(20)]
    arr = ArrayList()
    
    for i in L:
        arr.add(i)
        
    print(arr)
    print(type(arr))
    
    cad = String("Hola")
    