"""
Threads: 
"""

from threading import Thread, active_count, enumerate
from random import randint
from time import sleep


class ThreadMensajes(Thread):

    def __init__(self, nombre="", n=10):
        Thread.__init__(self, name=nombre)
        self.n = n

    def run(self):
        for i in range(self.n):
            print(f"{self.name} - ", f"mensaje {i+1}")
            sleep(randint(1, 3))
        print(self.name, "termina")


class ThreadRandom(Thread):

    def __init__(self, nombre="", n=10):
        Thread.__init__(self, name=nombre)
        self.n = n

    def run(self):
        for i in range(self.n):
            print(f"{self.name} - {i+1} -> ", randint(1, 10))
            sleep(randint(2, 4))
        print(self.name, "termina")


if __name__ == "__main__":
    m = ThreadMensajes("mensajes", 15)
    r = ThreadRandom("aleatorio", 13)

    m.start()
    r.start()

    print("num: hilos: ", active_count())
    print("hilos: ", enumerate())

    # main espera a que terminen los hilos
    m.join()
    r.join()

    print("main termina ...")
