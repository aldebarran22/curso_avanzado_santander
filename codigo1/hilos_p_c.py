"""
Implementación del productor-consumidor en Python
Solución M productores-N consumidores
"""

from threading import Thread, Lock, Semaphore
from random import randint
from time import sleep

num_muestras = 10
tam_buffer = 5

num_productores = 2
num_consumidores = 1


class Productor(Thread):
    def __init__(self, buffer, num_muestras, nombre):
        Thread.__init__(self, name=nombre)
        self.buffer = buffer
        self.num_muestras = num_muestras

    def run(self):
        for i in range(self.num_muestras):
            # Producir un item:
            numero = randint(1, 10)
            print(self.name, "GENERA -> ", numero)

            # Comprobar si hay hueco:
            self.buffer.sem_huecos.acquire()

            # Escribir el buffer el item:
            with self.buffer.mutex:
                self.buffer.buffer[self.buffer.ind_p] = numero
                print(self.buffer.buffer)
                self.buffer.ind_p = (self.buffer.ind_p + 1) % tam_buffer

            # Avisar que hay un nuevo item:
            self.buffer.sem_items.release()


class Consumidor(Thread):
    def __init__(self, buffer, num_muestras, nombre):
        Thread.__init__(self, name=nombre)
        self.buffer = buffer
        self.num_muestras = num_muestras

    def run(self):
        for i in range(self.num_muestras):

            # Comprobar si hay items:
            self.buffer.sem_items.acquire()

            # Recuperar un numero del buffer:
            with self.buffer.mutex:

                numero = self.buffer.buffer[self.buffer.ind_c]
                self.buffer.buffer[self.buffer.ind_c] = -1
                print(self.buffer.buffer)
                self.buffer.ind_c = (self.buffer.ind_c + 1) % num_muestras

            # Avisar que hay un nuevo hueco:
            self.buffer.sem_huecos.release()

            print(self.name, "CONSUME -> ", numero)


class TBuffer:
    def __init__(self):
        self.ind_c = 0
        self.ind_p = 0
        self.buffer = [-1] * tam_buffer
        self.mutex = Lock()
        self.sem_huecos = Semaphore(tam_buffer)
        self.sem_items = Semaphore(0)


if __name__ == "__main__":
    if num_muestras % num_productores != 0 or num_muestras % num_consumidores != 0:
        print("El número tiene que estar equilibrado entre el n. de prod/con")
        exit()

    # Calcular el numero de muestras por productor y consumidor:
    num_muestras_prod = num_muestras // num_productores
    num_muestras_con = num_muestras // num_consumidores

    productores = []
    consumidores = []

    buf = TBuffer()

    for i in range(num_productores):
        prod = Productor(buf, num_muestras_prod, f"P-{i+1}")
        prod.start()
        productores.append(prod)

    for i in range(num_consumidores):
        con = Consumidor(buf, num_muestras_con, f"C-{i+1}")
        con.start()
        consumidores.append(prod)

    for p in productores:
        p.join()

    for c in consumidores:
        c.join()
