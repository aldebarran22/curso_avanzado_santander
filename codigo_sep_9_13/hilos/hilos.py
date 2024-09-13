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
        pass

class ThreadRandom(Thread):

    def __init__(self, nombre="", n = 10):
        Thread.__init__(self, name=nombre)
        self.n = n

    def run(self):
        pass
