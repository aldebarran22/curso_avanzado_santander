"""
Codigo de ejemplo para descargar una URL
"""

import urllib.request as urllib2
from threading import Thread
from queue import Queue
import logging

# Establecer el nivel de configuración de logging:
# debug, info, warn, error, critical
logging.basicConfig(level=logging.DEBUG)

ficheros = 100
num_hilos = 5


def descargaURL(url):
    f = None
    numero = None

    try:
        f = urllib2.urlopen(url)
        logging.debug(f"Abrir url: {url}")

        numero = int(f.read())
        return numero

    except Exception as e:
        logging.error(e.getMessage())

    finally:
        if f != None:
            logging.debug(f"Cerrando url: {url}")
            f.close()


class Download(Thread):

    def __init__(self, ini, fin, q):
        Thread.__init__(self)
        self.ini = ini
        self.fin = fin
        self.q = q

    def run(self):
        logging.info(f"{self.name} Descarga de {self.ini} a {self.fin}")
        for i in range(self.ini, self.fin):
            url = f"http://localhost:8000/fich{i}.txt"
            numero = descargaURL(url)
            logging.info(f"{self.name} {url} {numero}")
            self.q.put(numero)


if __name__ == "__main__":

    if ficheros % num_hilos != 0:
        print("Cambiar el número de hilos")
        exit()

    L = []
    numFich = ficheros // num_hilos
    q = Queue(ficheros)
    limites = [(i * numFich, (i * numFich) + numFich) for i in range(num_hilos)]
    for i in range(num_hilos):
        hilo = Download(*limites[i], q)
        hilo.start()
        L.append(hilo)

    for h in L:
        h.join()

    lista = []
    while not q.empty():
        lista.append(q.get())
    lista.sort()
    print(lista[:5], lista[-5:])
