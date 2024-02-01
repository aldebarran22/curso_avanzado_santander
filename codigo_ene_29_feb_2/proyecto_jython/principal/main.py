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
from es.curso.clases import Usuario
from collections import deque, namedtuple

def coleccionesJython():
    L = [1,2,3,4,5,6,7]
    
    d = deque(L)
    d.append(-1)
    d.appendleft(-2)    
    print(d)
    d.rotate(5)
    print(d)
    
    CuentaBancaria = namedtuple("CuentaBancaria", ['sucursal','entidad','dc','numero'])
    cc = CuentaBancaria(1000,2000,99,1234567)
    print(cc.dc)
    print(cc)
    print(cc._asdict())
    

def crearColeccionUsuarios():
    L = []
    L.append(Usuario('admin','1234','admin@webmaster.es'))
    L.append(Usuario('admin2','abc','anonimo@webmaster.es'))
    L.append(Usuario('admin3','zaz','sistemas@webmaster.es'))
    
    print(L)

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
    #leerFichero()
    #crearColeccionUsuarios()
    coleccionesJython()