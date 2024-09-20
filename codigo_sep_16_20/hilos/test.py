

from threading import Thread, Lock

contador = 0
N = 1000000
mutex = Lock()

def sumar():
    global contador
    for i in range(N):
        mutex.acquire()
        contador+=1
        mutex.release()

def restar():
    global contador
    for i in range(N):
        with mutex:
            contador-=1

h1 = Thread(target=sumar)
h1.start()

h2 = Thread(target=restar)
h2.start()

h1.join()
h2.join()
print("contador: ", contador)