"""
Implementar el patrón estrategia con los
distintos métodos de ordenación de colecciones.

El contexto se encargará de generar una lista
de números aleatorios y cronometrar el tiempo
de ordenación de cada algoritmo.

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
    def __init__(self, clase, n):
        self.estrategias = clase.__subclasses__()
        self.L = [randint(1, 10000) for _ in range(n)]

    def crono(self):
        for algoritmo in self.estrategias:
            # Obtener una copia de la lista:
            unaLista = self.L.copy()

            # Instanciar la estrategia:
            est = algoritmo()
            nombreEst = est.__class__.__name__
            print('Probando ',nombreEst)

            t1 = datetime.now()
            est.ordenar(unaLista)
            t2 = datetime.now()

            print(nombreEst, "Tiempo de ordenación: ", t2 - t1)

if __name__ == '__main__':
    contexto = Contexto(Estrategia, 10000)
    contexto.crono()