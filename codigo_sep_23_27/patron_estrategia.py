"""
Patrón Estrategia modificado para saber que algoritmo es el más rápido con la
ordenación de una lista
"""

import abc
from datetime import datetime
from random import randint


class Estrategia(abc.ABC):

    @abc.abstractmethod
    def ordenar(self, unaLista):
        pass


class EstrategiaPython(Estrategia):

    def ordenar(self, unaLista):
        unaLista.sort()


class EstrategiaBurbuja(Estrategia):
    def ordenar(self, unaLista):
        for numPasada in range(len(unaLista) - 1, 0, -1):
            for i in range(numPasada):
                if unaLista[i] > unaLista[i + 1]:
                    temp = unaLista[i]
                    unaLista[i] = unaLista[i + 1]
                    unaLista[i + 1] = temp


class EstrategiaInsDirecta(Estrategia):

    def ordenar(self, unaLista):
        for indice in range(1, len(unaLista)):

            valorActual = unaLista[indice]
            posicion = indice

            while posicion > 0 and unaLista[posicion - 1] > valorActual:
                unaLista[posicion] = unaLista[posicion - 1]
                posicion = posicion - 1

            unaLista[posicion] = valorActual

class Contexto:

    def __init__(self, claseEstrategia, n=10000):
        self.claseEstrategia = claseEstrategia
        self.L = [randint(1,10000) for _ in range(n)]
        
    def cronometrar(self):
        for c in self.claseEstrategia.__subclasses__():
            obj = c()
            copia = self.L.copy()
            t1 = datetime.now()
            obj.ordenar(copia)
            t2 = datetime.now()
            intervalo = t2 - t1
            print(obj.__class__.__name__, intervalo)

if __name__ == '__main__':
    contexto = Contexto(Estrategia)            
    contexto.cronometrar()