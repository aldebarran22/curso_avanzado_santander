"""
Generar varios hilos que lanzan números aleatorios.
"""

from threading import Thread
from random import randint
from time import sleep


class Hilo(Thread):

    def __init__(self, nombre, n=10):
        Thread.__init__(self, name=nombre)
        self.n = n
        self.L = list()

    def run(self):
        for i in range(self.n):
            numero = randint(1, 30)
            self.L.append(numero)
            print(self.name, " num: ", numero)
            sleep(randint(1, 3))

        print(self.name, " ha terminado!")
        print(self.L)


if __name__ == "__main__":
    hilos = []
    nHilos = 5
    for i in range(nHilos):
        nombre = f"H-{i+1}"
        hilo = Hilo(nombre, randint(5, 10))
        hilo.start()
        hilos.append(hilo)

    print("main terminado!")
