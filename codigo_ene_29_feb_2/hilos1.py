"""
Crear dos hilos que heredan de la clase
threading.Thread
1) Lanza mensajes a la consola
2) Generar números aleatorios
"""

from threading import Thread


class Mensajes(Thread):
    def __init__(self, n=10):
        Thread.__init__(self, name="Mensajes")
        self.n = n

    def run(self):
        pass

class Aleatorio(Thread):
    def __init__(self, n=15):
        Thread.__init__(self, name="Aleatorio")
        self.n = n

    def run(self):
        pass