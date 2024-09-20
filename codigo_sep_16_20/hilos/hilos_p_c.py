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
                  
           # Generar un item:
           numero = randint(1,20)

           # Comprobar si tiene hueco
           self.buffer.sem_huecos.acquire()
           
           # Si tiene hueco, escribe el num. en exclusión mutua
           with self.buffer.mutex:
                # Colocar el numero en el buffer e incrementar el índice
                self.buffer.buffer[self.buffer.inc_p] = numero
                print(self.name,self.buffer.buffer,"<-",numero)
                self.buffer.inc_p = (self.buffer.inc_p + 1) % tam_buffer        

           # Avisar de que hay un nuevo item
           self.buffer.sem_items.release()

           sleep(randint(2,4))


class Consumidor(Thread):
    def __init__(self, buffer, num_muestras, nombre):
        Thread.__init__(self)
        self.buffer = buffer
        self.num_muestras = num_muestras


    def run(self):
        pass


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


   
