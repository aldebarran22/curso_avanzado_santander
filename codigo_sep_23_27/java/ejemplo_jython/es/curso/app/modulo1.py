'''
Created on 26-sep-2024

@author: Anton
'''

from java.util import ArrayList

if __name__ == '__main__':
    arr = ArrayList()
    
    for i in range(50):
        arr.add(i)
    
    print(arr[:5])