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
