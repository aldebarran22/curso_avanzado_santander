"""
Productor - Consumidor
Para N - M
"""

from threading import Thread, Lock, Semaphore
from random import randint
from time import sleep

num_muestras = 10
tam_buffer = 5

num_productores = 2
num_consumidores = 1


class TBuffer:
    def __init__(self):
        self.ind_c = 0
        self.ind_p = 0
        self.buffer = [-1] * tam_buffer
        self.mutex = Lock()
        self.sem_huecos = Semaphore(tam_buffer)
        self.sem_items = Semaphore(0)


class Productor(Thread):
    def __init__(self, buf, num_muestras_p, nombre):
        self.buf = buf
        self.num_muestras_p = num_muestras_p
        self.nombre = nombre

    def run(self):
        pass


class Consumidor(Thread):
    def __init__(self, buf, num_muestras_c, nombre):
        self.buf = buf
        self.num_muestras_c = num_muestras_c
        self.nombre = nombre

    def run(self):
        pass


if __name__ == "__main__":
    if num_muestras % num_productores != 0:
        print("El número de prod. no es múltiplo del num_muestras")
        exit()  # corta el script

    if num_muestras % num_consumidores != 0:
        print("El número de cons. no es múltiplo del num_muestras")
        exit()  # corta el script

    num_muestras_prod = num_muestras // num_productores
    num_muestras_con = num_muestras // num_consumidores

    buf = TBuffer()

    productores = []
    consumidores = []

    for i in range(num_productores):
        nombre = f"P-{(i+1)}"
        productor = Productor(buf, num_muestras_prod, nombre)
        productor.start()
        productores.append(productor)

    for i in range(num_consumidores):
        nombre = f"C-{(i+1)}"
        consumidor = Consumidor(buf, num_muestras_con, nombre)
        consumidor.start()
        consumidores.append(consumidor)

    for p in productores:
        p.join()

    for c in consumidores:
        c.join()
