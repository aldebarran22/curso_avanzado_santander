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

def grabar2(path, *matrices):
    #dicc = {"m"+str(i+1):m for i, m in enumerate(matrices)}
    np.savez_compressed(path, m1=matrices[0], m2=matrices[1], m3=matrices[2])

def load2(path):
    matrices = np.load(path)
    print("--------------------------")
    print(matrices['m2'])
    print()

if __name__ == '__main__':
    m = np.random.randint(1,100, (10, 15))
    m2 = np.random.randint(1,100, (5, 5))
    m3 = np.random.randint(1,100, (10, 10))

    grabarTxt(m, "../ficheros/matriz.csv")
    mCargada = cargarTxt("../ficheros/matriz.csv")
    print(mCargada)

    grabar2("../ficheros/matriz.npz", m, m2, m3)
    load2("../ficheros/matriz.npz")

    
