

from threading import Thread

contador = 0
N = 1000000

def sumar():
    global contador
    for i in range(N):
        contador+=1

def restar():
    global contador
    for i in range(N):
        contador-=1

h1 = Thread(target=sumar)
h1.start()

h2 = Thread(target=restar)
h2.start()

h1.join()
h2.join()
print("contador: ", contador)