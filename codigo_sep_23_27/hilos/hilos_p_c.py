"""
Implementación del productor-consumidor en Python
Solución M productores-N consumidores
"""

from threading import Thread, Lock, Semaphore
from random import randint
from time import sleep

num_muestras = 10
tam_buffer = 5

num_productores = 1
num_consumidores = 1


class Productor(Thread):
    def __init__(self, buffer, num_muestras, nombre):
        Thread.__init__(self, name=nombre)
        self.buffer = buffer
        self.num_muestras = num_muestras

    def run(self):
        for i in range(self.num_muestras):

            # Generar un item: número aleatorio
            numero = randint(1, 20)
            print(self.name, "PRODUCE", numero)

            # Comprobar si hay un hueco: sem_huecos
            self.buffer.sem_huecos.acquire()

            # modificar el buffer en excl. mutua
            with self.buffer.mutex:
                # escribir el número en el buffer
                self.buffer.buffer[self.buffer.ind_p] = numero
                print(self.buffer.buffer)

                # modificar el índice
                self.buffer.ind_p = (self.buffer.ind_p + 1) % tam_buffer

            # Avisar de que hay un nuevo item:
            self.buffer.sem_items.release()

            # Esperar x SG.
            sleep(randint(1, 3))

        print(self.name, "TERMINA!")


class Consumidor(Thread):
    def __init__(self, buffer, num_muestras, nombre):
        Thread.__init__(self, name=nombre)
        self.buffer = buffer
        self.num_muestras = num_muestras

    def run(self):
        for i in range(self.num_muestras):

            # comprobar si hay items
            self.buffer.sem_items.acquire()

            # modificar el buffer en excl. mutua
            with self.buffer.mutex:
                # quitar un numero del buffer
                numero = self.buffer.buffer[self.buffer.ind_c]
                self.buffer.buffer[self.buffer.ind_c] = -1
                print(self.buffer.buffer)

                # modificar el indice
                self.buffer.ind_c = (self.buffer.ind_c + 1) % tam_buffer

            # avisar del nuevo hueco
            self.buffer.sem_huecos.release()

            # consumir el elemento
            print(self.name, "CONSUME", numero)

            sleep(randint(2,4))

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
