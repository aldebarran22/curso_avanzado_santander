"""
Lanzar n hilos en paralelo para descargar 100 ficheros de un servidor
"""

from threading import Thread

"""
Codigo de ejemplo para descargar una URL
"""

import urllib.request as urllib2


class HiloURL(Thread):
    def __init__(self, ini, fin):
        Thread.__init__(self)
        self.ini = ini
        self.fin = fin

    def run(self):
        for i in range(self.ini, self.fin):
            url = f"http://localhost:8000/fich{i}.txt"
            numero = self.descargaURL(url)
            print(self.getName(), " url: ", url, "numero:", numero)

    def descargaURL(self, url):
        f = None
        numero = None

        try:
            f = urllib2.urlopen(url)
            numero = int(f.read())
            print(numero)
            return numero

        except Exception as e:
            print("ERROR: ", e)

        finally:
            if f != None:
                f.close()


if __name__ == "__main__":
    num_hilos = 4
    num_ficheros = 100

    num_ficheros_hilos = num_ficheros // num_hilos
    L = []
    for i in range(0, num_ficheros, num_ficheros_hilos):
        h = HiloURL(i, i + num_ficheros_hilos)
        h.start()
        L.append(h)

    for h in L:
        h.join()
