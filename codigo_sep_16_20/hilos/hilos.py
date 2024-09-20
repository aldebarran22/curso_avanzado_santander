"""
Implementación de hilos con la clase Thread y
problemas al esperar un hilo: join
"""

from threading import Thread, enumerate, activeCount
from random import randint
from time import sleep


class ThreadRandom(Thread):

    def __init__(self, nombre, n):
        Thread.__init__(self, name=nombre)
        self.L = []
        self.n = n

    def run(self):
        for i in range(self.n):
            num = randint(1, 10)
            print(self.name, "==>", num)
            self.L.append(num)
            sleep(randint(1, 3))
        print("Termina: ", self.name)


if __name__ == "__main__":
    hilos = []
    n_hilos = 3
    for i in range(n_hilos):
        nombre = f"Hilo-{i+1}"
        hilo = ThreadRandom(nombre, randint(5, 10))
        hilo.start()
        hilos.append(hilo)

    print("HILOS: ", enumerate())
    print("ACTIVOS: ", activeCount())

    for hilo in hilos:
        hilo.join()

    print("Termina main")
