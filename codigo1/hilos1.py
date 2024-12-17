"""
Crear hilos, listas de hilos y problemas con join (al esperar a que
terminen los hilos)
"""

from threading import Thread
from time import sleep
from random import randint


class Mensajes(Thread):

    def __init__(self, n, nombre):
        Thread.__init__(self, name=nombre)
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.name, "mensaje", (i + 1))
            sleep(randint(1, 3))
        print("Termina", self.name)


if __name__ == "__main__":
    L = []
    for i in range(3):
        nombre = f"H-{i+1}"
        hilo = Mensajes(randint(5, 10), nombre)
        hilo.start()
        L.append(hilo)

    for hilo in L:
        hilo.join()

    print('Termina main')
