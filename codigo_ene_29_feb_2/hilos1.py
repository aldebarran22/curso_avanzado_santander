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
    def __init__(self, n=10):
        Thread.__init__(self, name="Mensajes")
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
    m = Mensajes(12)
    a = Aleatorio(13)

    # Poner en marcha los hilos
    m.start()
    a.start()

    # Esperar a que terminen los hilos:
    m.join()
    a.join()

    print("main termina")
