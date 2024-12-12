"""
Patrón Estrategia con los métodos de ordenación de una lista
El contexto se va a encargar de cronometrar el tiempo de ejecución
de cada algoritmo.
"""

import abc

class Estrategia(abc.ABC):

    @abc.abstractmethod
    def ordenar(self, unaLista):
        pass

class EstrategiaBurbuja(Estrategia):

    def ordenar(self, unaLista):
        for numPasada in range(len(unaLista)-1,0,-1):
            for i in range(numPasada):
                if unaLista[i]>unaLista[i+1]:
                    temp = unaLista[i]
                    unaLista[i] = unaLista[i+1]
                    unaLista[i+1] = temp

class EstrategiaInsDirecta(Estrategia):

    def ordenar(self, unaLista):
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



