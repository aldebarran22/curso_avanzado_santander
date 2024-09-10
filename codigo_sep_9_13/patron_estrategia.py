"""
Patrón estrategia con una variación para cronometrar cual es
la estrategia más rápida para ordenar una lista de N números
aleatorios
"""

import abc

class Estrategia(abc.ABC):

    @abc.abstractmethod
    def ordenar(self,unaLista):
        pass
        
class EstrategiaBurbuja(Estrategia):

    def ordenar(self,unaLista):
        for numPasada in range(len(unaLista)-1,0,-1):
            for i in range(numPasada):
                if unaLista[i]>unaLista[i+1]:
                    temp = unaLista[i]
                    unaLista[i] = unaLista[i+1]
                    unaLista[i+1] = temp

class EstrategiaPython(Estrategia):
    def ordenar(self,unaLista):
        unaLista.sort()


class EstrategiaInsDirecta(Estrategia):

    def ordenar(self,unaLista):
        for indice in range(1,len(unaLista)):

            valorActual = unaLista[indice]
            posicion = indice

            while posicion>0 and unaLista[posicion-1]>valorActual:
                unaLista[posicion]=unaLista[posicion-1]
                posicion = posicion-1

            unaLista[posicion]=valorActual






