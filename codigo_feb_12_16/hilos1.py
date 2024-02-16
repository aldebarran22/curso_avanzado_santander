"""
Hilos en Python
"""
from threading import Thread
from time import sleep

class Mensajes(Thread):

    def __init__(self, nombre, n=10):
        Thread.__init__(self, name=nombre)
        self.n = n
    
    def run(self):
        for i in range(self.n):
            print("Hilo:",self.getName()," mensaje:",i)
            sleep(1)
        print("Fin hilo: ",self.getName())

if __name__ == '__main__':
    L = []
    for i in range(3):
        h = Mensajes(f"H-{i}", 8)
        L.append(h)
        h.start()
    
    for h in L:
        h.join()


