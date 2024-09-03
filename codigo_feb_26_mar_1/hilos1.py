"""
Crear varios hilos
"""

from threading import Thread
from time import sleep
from random import randint


class Hilo(Thread):

    def __init__(self, nombre, n=10):
        Thread.__init__(self, name=nombre)
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.getName(), " mensaje: ", (i + 1))
            sleep(randint(0, 3))
        print(self.getName(), "termina!")


if __name__ == "__main__":
    L = []
    nHilos = 4
    for i in range(nHilos):
        hilo = Hilo(f"Hilo-{i+1}", randint(5, 10))
        hilo.start()
        L.append(hilo)

    for hilo in L:
        hilo.join()

    print("Thread-Main termina!")
