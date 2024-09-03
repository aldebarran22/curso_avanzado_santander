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
num_consumidores = 2


class Productor(Thread):
    def __init__(self, buffer, num_muestras, nombre):
        Thread.__init__(self, name=nombre)
        self.buf = buffer
        self.num_muestras = num_muestras

    def run(self):
        for i in range(self.num_muestras):
            numero = randint(1, 10)
            print(self.getName(), "genera", numero)
            # Comprobar si hay sitio en el buffer
            self.buf.sem_huecos.acquire()
            with self.buf.mutex:
                print(self.getName(), " ==> ", numero)
                self.buf.buffer[self.buf.ind_p] = numero
                print(self.buf.buffer)
                print()
                self.buf.ind_p = (self.buf.ind_p + 1) % tam_buffer
            # Avisar al consumidor: ya tienes un item:
            self.buf.sem_items.release()
            sleep(randint(1, 3))


class Consumidor(Thread):
    def __init__(self, buffer, num_muestras, nombre):
        Thread.__init__(self, name=nombre)
        self.buf = buffer
        self.num_muestras = num_muestras

    def run(self):
        for i in range(self.num_muestras):
            # Comprobar si hay un item:
            self.buf.sem_items.acquire()
            with self.buf.mutex:
                numero = self.buf.buffer[self.buf.ind_c]
                print(self.getName(), " <== ", numero)
                self.buf.buffer[self.buf.ind_c] = -1
                print(self.buf.buffer)
                print()
                self.buf.ind_c = (self.buf.ind_c + 1) % tam_buffer
            # Avisar al productor: hay un hueco nuevo
            self.buf.sem_huecos.release()
            print(self.getName(), "consume", numero)
            sleep(randint(2, 4))


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

    # Calcular el numero de muestra por productor y consumidor:
    num_muestras_prod = num_muestras // num_productores
    num_muestras_con = num_muestras // num_consumidores

    buf = TBuffer()

    productores = []
    consumidores = []

    for i in range(num_productores):
        nombre = f"P-{i+1}"
        productor = Productor(buf, num_muestras_prod, nombre)
        productor.start()
        productores.append(productor)

    for i in range(num_consumidores):
        nombre = f"C-{i+1}"
        consumidor = Consumidor(buf, num_muestras_con, nombre)
        consumidor.start()
        consumidores.append(consumidor)

    for p in productores:
        p.join()

    for c in consumidores:
        c.join()
