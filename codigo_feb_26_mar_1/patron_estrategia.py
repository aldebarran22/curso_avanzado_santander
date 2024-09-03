"""
Patrón estrategia modificado para cronometrar tiempos de ejecución
de los alg. de ordenación
"""

import abc
from datetime import datetime
from random import randint


class Estrategia(abc.ABC):

    @abc.abstractmethod
    def ordenar(self, unaLista):
        pass


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


class EstrategiaPython(Estrategia):

    def ordenar(self, unaLista):
        unaLista.sort()


class Contexto:

    def __init__(self, claseEstrategia, n):
        self.clase = claseEstrategia
        self.n = n

    def crono(self):
        L = [randint(0, 100000) for i in range(self.n)]
        for c in self.clase.__subclasses__():
            Lcopia = L.copy()
            objeto = c() # c es cada una de las estrategias.
            t1 = datetime.now()
            objeto.ordenar(Lcopia)
            t2 = datetime.now()
            print(c.__name__, t2 - t1)


if __name__ == "__main__":
    contexto = Contexto(Estrategia, 12000)
    contexto.crono()
