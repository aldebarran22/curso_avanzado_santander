'''
Created on 01-feb-2024

@author: Anton
'''

# Importar alguna clase de java
from java.lang import String
from java.util import ArrayList
from java.util import Scanner
from java.io import File

from random import randint

def leerFichero():
    scan = None
    try:
        scan = Scanner(File('D:/OneDrive/Escritorio/python_avanzado_santander/practicas/avanzado2/pandas/names/yob1990.txt'))
        while scan.hasNextLine():
            print(scan.nextLine())
    except Exception as e:
        print(e)
    finally:
        if scan: scan.close()

def cargarColeccion():
    arr = ArrayList()
    arr.add(String("Alemania"))
    arr.add("Francia")
    arr.add("Italia")
    print(arr)
    
    for s in arr:
        print(s, type(s))

if __name__ == '__main__':
    #cargarColeccion()
    leerFichero()