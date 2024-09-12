'''
Created on 12-sep-2024

@author: Anton
'''

from java.util import Random


if __name__ == '__main__':
    r = Random()
    L = list()
    
    for i in range(25):
        L.append(r.nextInt())
        
    print(L)
