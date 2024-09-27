"""
Codigo de ejemplo para descargar una URL
"""

from threading import Thread
from queue import Queue
import urllib.request as urllib2


class Download(Thread):

    def __init__(self, ini, fin, q):
        Thread.__init__(self)
        self.ini = ini
        self.fin = fin
        self.q = q

    def run(self):
        for i in range(self.ini, self.fin):
            url = f"http://localhost:8000/fich{i}.txt"
            numero = self.descargaURL(url)
            print(self.name, url, numero)
            self.q.put(numero)

    def descargaURL(self, url):
        f = None
        numero = None

        try:
            f = urllib2.urlopen(url)
            numero = int(f.read())
            return numero

        except Exception as e:
            print("ERROR: ", e)

        finally:
            if f != None:
                f.close()


if __name__ == "__main__":
    num_ficheros = 100
    num_hilos = 5
    num_fich_hilo = num_ficheros // num_hilos
    hilos = []
    params = [
        (i * num_fich_hilo, i * num_fich_hilo + num_fich_hilo) for i in range(num_hilos)
    ]
    q = Queue(num_ficheros)
    for i in range(num_hilos):
        h = Download(*params[i], q)
        h.start()
        hilos.append(h)

    for h in hilos:
        h.join()
    L = list()
    while not q.empty():
        L.append(q.get())
    L.sort()
    print(L[:10], "...", L[-10:])
