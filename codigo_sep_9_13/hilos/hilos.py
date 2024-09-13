"""
Threads: 
"""

from threading import Thread
from random import randint

class ThreadMensajes(Thread):

    def __init__(self, nombre="", n = 10):
        Thread.__init__(self, name=nombre)
        self.n = n

    def run(self):
        for i in range(self.n):
            print(f"{self.name} - ", f"mensaje {i+1}" )
        print(self.name,"termina")

class ThreadRandom(Thread):

    def __init__(self, nombre="", n = 10):
        Thread.__init__(self, name=nombre)
        self.n = n

    def run(self):
        for i in range(self.n):
            print(f"{self.name} - {i+1} -> ", randint(1,10))
        print(self.name,"termina")

if __name__ == '__main__':
    m = ThreadMensajes("mensajes", 15)
    r = ThreadRandom("aleatorio", 13)

    m.start()
    r.start()

    print('main termina ...')
