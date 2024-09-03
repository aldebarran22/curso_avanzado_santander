"""
Hilos en Python
"""

from threading import Thread, active_count
from time import sleep
from random import randint


class Mensajes(Thread):

    def __init__(self, nombre, n=10):
        Thread.__init__(self, name=nombre)
        self.n = n

    def run(self):
        for i in range(self.n):
            print("Hilo:", self.getName(), " mensaje:", i)
            sleep(randint(1, 3))
        print("Fin hilo: ", self.getName())


if __name__ == "__main__":
    L = []
    for i in range(3):
        h = Mensajes(f"H-{i}", 8)
        L.append(h)
        h.start()

    print("Hilos activos: ", active_count())
    for h in L:
        h.join()
