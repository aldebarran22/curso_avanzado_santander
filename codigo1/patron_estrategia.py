"""
Patrón Estrategia: métodos de ordenación. 
En este caso se utiliza el contexto para medir tiempos de ejecución
de los algoritmos.
"""

import abc
from datetime import datetime 
from random import randint
class Estrategia(abc.ABC):

    @abc.abstractmethod
    def ordenar(self, unaLista):
        pass

class EstrategiaBurbuja(Estrategia):

    def ordenamientoBurbuja(self, unaLista):
        for numPasada in range(len(unaLista)-1,0,-1):
            for i in range(numPasada):
                if unaLista[i]>unaLista[i+1]:
                    temp = unaLista[i]
                    unaLista[i] = unaLista[i+1]
                    unaLista[i+1] = temp


class EstrategiaInsDirecta(Estrategia):

    def ordenamientoPorInsercion(self,unaLista):
        for indice in range(1,len(unaLista)):

            valorActual = unaLista[indice]
            posicion = indice

            while posicion>0 and unaLista[posicion-1]>valorActual:
                unaLista[posicion]=unaLista[posicion-1]
                posicion = posicion-1

            unaLista[posicion]=valorActual


class EstrategiaPython(Estrategia):

    def ordenar(self, unaLista):
        unaLista.sort()


