"""
Entrada / Salida en numpy
Una sola matriz:
npy -> binario (no Excel)
txt -> ascii (para Excel)

Varias matrices:
npz (se trata como un diccionario)
"""

import numpy as np

def grabarTxt(m, path):
    np.savetxt(path, m, fmt='%d', delimiter=';')


def cargarTxt(path):
    return np.loadtxt(path, delimiter=';', dtype="u1")

if __name__ == '__main__':
    m = np.random.randint(1,100, (10, 15))
    grabarTxt(m, "../ficheros/matriz.csv")
    m2 = cargarTxt("../ficheros/matriz.csv")
    print(m2)
    
