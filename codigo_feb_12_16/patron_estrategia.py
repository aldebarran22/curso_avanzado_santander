"""
Implementación del patrón estrategia.
3 métodos de ordenación. El contexto se utiliza para cronometrar
tiempos de ejecución.
"""

import abc
from random import randint
from datetime import datetime


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


class EstrategiaIDirecta(Estrategia):

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

    def __init__(self, n, clase):
        self.n = n
        self.clase = clase
        self.unaLista = [randint(1, 10000) for _ in range(n)]

    def cronometrarEstrategias(self):

        for algoritmo in self.clase.__subclasses__():
            print(f"Prueba con {algoritmo.__name__}")
            L = self.unaLista.copy()
            # Crear cada una de las estrategias:
            objeto = algoritmo()

            t1 = datetime.now()
            objeto.ordenar(L)
            t2 = datetime.now()

            print("Tiempo de ordenación: ", t2 - t1, "para ", self.n, "elementos")
            print()


if __name__ == "__main__":
    n = 10000
    contexto = Contexto(n, Estrategia)
    contexto.cronometrarEstrategias()
