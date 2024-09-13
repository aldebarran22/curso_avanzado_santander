"""
Implementación del productor-consumidor en Python
Solución M productores-N consumidores
"""

from threading import Thread, Lock, Semaphore
from random import randint
from time import sleep

num_muestras = 12
tam_buffer = 5

num_productores = 2
num_consumidores = 3


class Productor(Thread):
    def __init__(self, buffer, num_muestras, nombre):
        Thread.__init__(self, name=nombre)
        self.buffer = buffer
        self.num_muestras = num_muestras

    def run(self):
        for i in range(self.num_muestras):
            # Generar un item:
            item = randint(0, 10)
            print(self.name, "GENERA", item)

            # Comprobar si hay hueco:
            self.buffer.sem_huecos.acquire()

            # Modificar el buffer:en exclusión mutua
            with self.buffer.mutex:

                # Escribir el número en el buffer:
                self.buffer.buffer[self.buffer.ind_p] = item

                # Actualizar el indice:
                self.buffer.ind_p = (self.buffer.ind_p + 1) % tam_buffer

                print(self.name, self.buffer.buffer)

            # Avisar de que hay un item:
            self.buffer.sem_items.release()

            sleep(randint(2, 4))

        print(self.name, "TERMINA!")


class Consumidor(Thread):
    def __init__(self, buffer, num_muestras, nombre):
        Thread.__init__(self, name=nombre)
        self.buffer = buffer
        self.num_muestras = num_muestras

    def run(self):
        for i in range(self.num_muestras):

            # Comprobar si tenemos un item:
            self.buffer.sem_items.acquire()

            # Modificar el buffer:
            with self.buffer.mutex:

                # Recuperar el item:
                item = self.buffer.buffer[self.buffer.ind_c]

                # Vaciar la casilla:
                self.buffer.buffer[self.buffer.ind_c] = -1

                # Modificar el indice:
                self.buffer.ind_c = (self.buffer.ind_c + 1) % tam_buffer

            # Avisar del nuevo hueco:
            self.buffer.sem_huecos.release()

            # Consumir el item:
            print(self.name, "CONSUME", item)

            sleep(randint(1, 3))

        print(self.name, "TERMINA!")


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

    # Crear la lista de productores y de consumidores:
    productores = []
    consumidores = []

    for i in range(num_productores):
        nombre = f"P-{i+1}"
        prod = Productor(buf, num_muestras_prod, nombre)
        prod.start()
        productores.append(prod)

    for i in range(num_consumidores):
        nombre = f"C-{i+1}"
        con = Consumidor(buf, num_muestras_con, nombre)
        con.start()
        consumidores.append(con)

    for p in productores:
        p.join()

    for c in consumidores:
        c.join()
