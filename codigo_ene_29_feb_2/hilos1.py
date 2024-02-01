"""
Crear dos hilos que heredan de la clase
threading.Thread
1) Lanza mensajes a la consola
2) Generar números aleatorios
"""

from threading import Thread
from random import randint
from time import sleep


class Mensajes(Thread):
    def __init__(self, n=10, i=0):
        nombre = f"hilo-{i}"
        Thread.__init__(self, name=nombre)
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.getName(), " ", (i + 1))
            sleep(randint(1, 3))


class Aleatorio(Thread):
    def __init__(self, n=15):
        Thread.__init__(self, name="Aleatorio")
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.getName(), " ", randint(1, 50))
            sleep(randint(1, 2))


if __name__ == "__main__":
    L = []
    for i in range(1, 6):
        m = Mensajes(randint(5, 10), i)
        m.start()
        L.append(m)

    a = Aleatorio(13)
    a.start()

    for h in L:
        h.join()

    # Esperar a que terminen los hilos:
    a.join()

    print("main termina")
