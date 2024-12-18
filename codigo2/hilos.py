"""
Crear varios hilos y almacenarlos en una lista.
Uso de join()
"""

from threading import Thread
from random import randint
from time import sleep


class Mensaje(Thread):

    def __init__(self, n, nombre):
        Thread.__init__(self, name=nombre)
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.name, "MENSAJE: ", (i + 1))
            sleep(randint(1, 3))
        print("Termina hilo: ", self.name)


if __name__ == "__main__":
    L = []
    numHilos = 4
    for i in range(numHilos):
        hilo = Mensaje(randint(5, 10), f"H-{i+1}")
        L.append(hilo)
        hilo.start()

    for hilo in L:
        hilo.join()

    print('main termina!')
