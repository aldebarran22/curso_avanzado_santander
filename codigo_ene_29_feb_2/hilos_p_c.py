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

if __name__ == '__main__':
    if num_muestras % num_productores != 0:
        print('El número de prod. no es múltiplo del num_muestras')
        exit() # corta el script

    if num_muestras % num_consumidores != 0:
        print('El número de cons. no es múltiplo del num_muestras')
        exit() # corta el script

