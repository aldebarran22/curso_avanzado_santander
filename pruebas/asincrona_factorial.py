import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, wait

def fact(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

if __name__ == "__main__":

    t0 = time.time()

    with ThreadPoolExecutor(max_workers=50) as e:
        fs = {e.submit(fact, i):i for i in range(4000)}
        wait(fs)

    t1 = time.time()

    with ProcessPoolExecutor() as e:
        fs = {e.submit(fact, i):i for i in range(4000)}
        wait(fs)

    t2 = time.time()

    print(f"Ejecución con hilos: {t1-t0:.2f}s")
    print(f"Ejecución con procesos: {t2-t1:.2f}s")
        
    