from time import sleep
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed


def action(numero, retardo):
    print('inicio de %d (espera de %d)' % (numero, retardo) )
    sleep(retardo)
    print('fin de %d (espera de %d)' % (numero, retardo) )


if __name__=='__main__':
    retardos = [2,5,3,6,1]

    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(action, n, d): d for n, d in enumerate(retardos)}
           
        for future in as_completed(futures):
            print('#Completada: %s', future)

